#!/usr/bin/env python3
import os
import sqlite3
import random
import numpy as np
from PIL import Image

import torch
import torch.nn as nn
import torch.optim as optim
import clip


# ---------------- Hardcoded paths ----------------
FRAMES_DIR = "./frames"
TRUE_DIR = "./true"
REF_PATH = "./ref.png"
DB_PATH = "embeddings.db"

# ---------------- Hardcoded training params ----------------
MODEL_NAME = "ViT-L/14"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

BATCH_SIZE = 256
EPOCHS = 10
LR = 1e-3
WEIGHT_DECAY = 1e-4
VAL_SPLIT = 0.15
SEED = 1337

CHECKPOINT_PATH = "checkpoints/useful_classifier_mlp.pt"


# ---------------- Model: MLP on embeddings (ref + frame) ----------------
class UsefulClassifier(nn.Module):
    def __init__(self, embed_dim, hidden=1024, dropout=0.2):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2 * embed_dim, hidden),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden, hidden // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden // 2, 2)  # logits for [NOT_USEFUL, USEFUL]
        )

    def forward(self, ref_emb, frame_emb):
        x = torch.cat([ref_emb, frame_emb], dim=1)  # [B, 2D]
        return self.net(x)


# ---------------- Utils ----------------
def set_seed(seed=1337):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def list_image_paths(dir_path):
    exts = (".png", ".jpg", ".jpeg", ".webp")
    out = []
    for name in os.listdir(dir_path):
        if name.lower().endswith(exts):
            out.append(os.path.join(dir_path, name))
    return sorted(out)


def normalize_unit(x):
    x = x.astype(np.float32, copy=False)
    n = np.linalg.norm(x, axis=1, keepdims=True) + 1e-12
    return x / n


def load_embedding_vector(conn, db_path_str, dtype=np.float32):
    row = conn.execute("SELECT vector FROM embeddings WHERE path = ?", (db_path_str,)).fetchone()
    if row is None:
        return None
    blob = row[0]
    vec = np.frombuffer(blob, dtype=dtype)
    return vec


def main():
    set_seed(SEED)

    if not os.path.exists(FRAMES_DIR):
        raise FileNotFoundError(f"Missing {FRAMES_DIR}")
    if not os.path.exists(TRUE_DIR):
        raise FileNotFoundError(f"Missing {TRUE_DIR}")
    if not os.path.exists(REF_PATH):
        raise FileNotFoundError(f"Missing {REF_PATH}")
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Missing {DB_PATH}")

    # Label source: membership in ./true (primary label)
    true_paths = set(list_image_paths(TRUE_DIR))  # USEFUL
    frame_paths = list_image_paths(FRAMES_DIR)   # ALL frames

    conn = sqlite3.connect(DB_PATH)

    useful_vecs = []
    not_useful_vecs = []
    missing_embeddings = 0

    for p in frame_paths:
        vec = load_embedding_vector(conn, p)
        if vec is None:
            missing_embeddings += 1
            continue
        if p in true_paths:
            useful_vecs.append(vec)       # y=1
        else:
            not_useful_vecs.append(vec)   # y=0

    conn.close()

    if len(useful_vecs) == 0 or len(not_useful_vecs) == 0:
        raise RuntimeError(
            "Need both classes with embeddings present.\n"
            f"USEFUL={len(useful_vecs)} NOT_USEFUL={len(not_useful_vecs)} "
            f"(missing={missing_embeddings})."
        )

    X = np.stack(useful_vecs + not_useful_vecs).astype(np.float32)  # [N, D]
    y = np.array([1] * len(useful_vecs) + [0] * len(not_useful_vecs), dtype=np.int64)  # [N]
    X = normalize_unit(X)

    # Compute ref CLIP embedding (primary measure)
    model, preprocess = clip.load(MODEL_NAME, device=DEVICE)
    model.eval()
    with torch.no_grad():
        ref_img = Image.open(REF_PATH).convert("RGB")
        ref_in = preprocess(ref_img).unsqueeze(0).to(DEVICE)
        ref_emb = model.encode_image(ref_in).float().cpu().numpy()  # [1, D]
    ref_emb = normalize_unit(ref_emb)[0]  # [D]

    # Train/val split
    N = len(X)
    idx = np.arange(N)
    np.random.shuffle(idx)
    n_val = int(N * VAL_SPLIT)
    val_idx = idx[:n_val]
    tr_idx = idx[n_val:]

    X_tr, y_tr = X[tr_idx], y[tr_idx]
    X_va, y_va = X[val_idx], y[val_idx]

    D = X.shape[1]
    net = UsefulClassifier(embed_dim=D).to(DEVICE)
    crit = nn.CrossEntropyLoss()
    opt = optim.AdamW(net.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)

    ref_tr = torch.tensor(ref_emb, dtype=torch.float32, device=DEVICE).unsqueeze(0)  # [1, D]
    ref_va = torch.tensor(ref_emb, dtype=torch.float32, device=DEVICE).unsqueeze(0)  # [1, D]

    def run_epoch(Xb, yb, train=True):
        if train:
            net.train()
        else:
            net.eval()

        total_loss = 0.0
        correct = 0
        total = 0

        for i in range(0, len(Xb), BATCH_SIZE):
            xb = torch.tensor(Xb[i:i + BATCH_SIZE], dtype=torch.float32, device=DEVICE)
            y_batch = torch.tensor(yb[i:i + BATCH_SIZE], dtype=torch.long, device=DEVICE)

            rb = ref_tr.expand(xb.size(0), -1)

            if train:
                opt.zero_grad(set_to_none=True)
                logits = net(rb, xb)
                loss = crit(logits, y_batch)
                loss.backward()
                opt.step()
            else:
                with torch.no_grad():
                    logits = net(rb, xb)
                    loss = crit(logits, y_batch)

            total_loss += loss.item() * xb.size(0)
            pred = logits.argmax(dim=1)
            correct += (pred == y_batch).sum().item()
            total += xb.size(0)

        return total_loss / total, correct / total

    for epoch in range(1, EPOCHS + 1):
        tr_loss, tr_acc = run_epoch(X_tr, y_tr, train=True)
        va_loss, va_acc = run_epoch(X_va, y_va, train=False)
        print(f"Epoch {epoch:02d} | train loss {tr_loss:.4f} acc {tr_acc:.3f} | val loss {va_loss:.4f} acc {va_acc:.3f}")

    os.makedirs(os.path.dirname(CHECKPOINT_PATH), exist_ok=True)
    torch.save(net.state_dict(), CHECKPOINT_PATH)
    print(f"Saved: {CHECKPOINT_PATH}")


if __name__ == "__main__":
    main()
