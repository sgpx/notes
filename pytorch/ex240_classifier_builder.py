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

# ---------------- Configuration ----------------
FRAMES_DIR = os.path.abspath("./frames")
TRUE_DIR = os.path.abspath("./true")
REF_PATH = os.path.abspath("./ref.png")
DB_PATH = "embeddings.db"
CHECKPOINT_PATH = "checkpoints/useful_classifier_mlp.pt"

MODEL_NAME = "ViT-L/14"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

BATCH_SIZE = 256
EPOCHS = 10
LR = 1e-3
WEIGHT_DECAY = 1e-4
VAL_SPLIT = 0.15
SEED = 1337

# ---------------- Model ----------------
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
            nn.Linear(hidden // 2, 2)
        )

    def forward(self, ref_emb, frame_emb):
        x = torch.cat([ref_emb, frame_emb], dim=1)
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
    for root, _, files in os.walk(dir_path):
        for name in files:
            if name.lower().endswith(exts):
                out.append(os.path.abspath(os.path.join(root, name)))
    return sorted(out)

def normalize_unit(x):
    x = x.astype(np.float32, copy=False)
    n = np.linalg.norm(x, axis=1, keepdims=True) + 1e-12
    return x / n

def load_embedding_vector(conn, absolute_path):
    # 1. Try the exact path
    row = conn.execute("SELECT vector FROM embeddings WHERE path = ?", (absolute_path,)).fetchone()
    if row: return np.frombuffer(row[0], dtype=np.float32)

    # 2. Try just the filename (e.g., 'frame_000001.png')
    filename = os.path.basename(absolute_path)
    row = conn.execute("SELECT vector FROM embeddings WHERE path = ?", (filename,)).fetchone()
    if row: return np.frombuffer(row[0], dtype=np.float32)

    # 3. Try a relative path format (e.g., './frames/frame_000001.png')
    # This matches the format that passed your test.py
    rel_path = "./frames/" + filename
    row = conn.execute("SELECT vector FROM embeddings WHERE path = ?", (rel_path,)).fetchone()
    if row: return np.frombuffer(row[0], dtype=np.float32)

    return None

def main():
    set_seed(SEED)

    # Validate paths
    for p in [FRAMES_DIR, TRUE_DIR, REF_PATH, DB_PATH]:
        if not os.path.exists(p):
            raise FileNotFoundError(f"Missing required path: {p}")

    # Prepare Data
    true_paths = set(list_image_paths(TRUE_DIR))
    frame_paths = list_image_paths(FRAMES_DIR)

    conn = sqlite3.connect(DB_PATH)
    useful_vecs, not_useful_vecs = [], []
    print("Building lookup map...")
    lookup_map = {}
    for row in conn.execute("SELECT path, vector FROM embeddings"):
        filename = os.path.basename(row[0])
        lookup_map[filename] = np.frombuffer(row[1], dtype=np.float32)

    useful_vecs, not_useful_vecs = [], []
    for p in frame_paths:
        filename = os.path.basename(p)
        vec = lookup_map.get(filename)
        
        if vec is not None:
            # Check membership based on filename
            if filename in {os.path.basename(tp) for tp in true_paths}:
                useful_vecs.append(vec)
            else:
                not_useful_vecs.append(vec)
    print("Loading embeddings...")
    for p in frame_paths:
        vec = load_embedding_vector(conn, p)
        if vec is not None:
            if p in true_paths:
                useful_vecs.append(vec)
            else:
                not_useful_vecs.append(vec)
    conn.close()

    if not useful_vecs or not not_useful_vecs:
        raise RuntimeError(f"Need both classes. USEFUL={len(useful_vecs)}, NOT_USEFUL={len(not_useful_vecs)}")

    X = np.stack(useful_vecs + not_useful_vecs).astype(np.float32)
    y = np.array([1] * len(useful_vecs) + [0] * len(not_useful_vecs), dtype=np.int64)
    X = normalize_unit(X)

    # Calculate class weights for loss (Important for imbalanced datasets)
    # Weight = total / (num_classes * count_per_class)
    n_samples = len(y)
    weight = torch.tensor([n_samples / (2 * len(not_useful_vecs)), 
                           n_samples / (2 * len(useful_vecs))], 
                          dtype=torch.float32, device=DEVICE)

    # Ref Embedding
    model, preprocess = clip.load(MODEL_NAME, device=DEVICE)
    model.eval()
    with torch.no_grad():
        ref_img = Image.open(REF_PATH).convert("RGB")
        ref_in = preprocess(ref_img).unsqueeze(0).to(DEVICE)
        ref_emb = model.encode_image(ref_in).float().cpu().numpy()
    ref_emb = normalize_unit(ref_emb)[0]

    # Split
    idx = np.random.permutation(len(X))
    n_val = int(len(X) * VAL_SPLIT)
    tr_idx, va_idx = idx[n_val:], idx[:n_val]
    X_tr, y_tr = X[tr_idx], y[tr_idx]
    X_va, y_va = X[va_idx], y[va_idx]

    # Training setup
    net = UsefulClassifier(embed_dim=X.shape[1]).to(DEVICE)
    crit = nn.CrossEntropyLoss(weight=weight)
    opt = optim.AdamW(net.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)

    ref_tr = torch.tensor(ref_emb, dtype=torch.float32, device=DEVICE).unsqueeze(0)
    ref_va = torch.tensor(ref_emb, dtype=torch.float32, device=DEVICE).unsqueeze(0)

    def run_epoch(Xb, yb, train=True):
        net.train() if train else net.eval()
        total_loss, correct, total = 0.0, 0, 0
        for i in range(0, len(Xb), BATCH_SIZE):
            xb = torch.tensor(Xb[i:i + BATCH_SIZE], device=DEVICE)
            yb_batch = torch.tensor(yb[i:i + BATCH_SIZE], device=DEVICE)
            rb = ref_tr.expand(xb.size(0), -1)

            if train:
                opt.zero_grad(set_to_none=True)
                logits = net(rb, xb)
                loss = crit(logits, yb_batch)
                loss.backward()
                opt.step()
            else:
                with torch.no_grad():
                    logits = net(rb, xb)
                    loss = crit(logits, yb_batch)

            total_loss += loss.item() * xb.size(0)
            correct += (logits.argmax(dim=1) == yb_batch).sum().item()
            total += xb.size(0)
        return total_loss / total, correct / total

    for epoch in range(1, EPOCHS + 1):
        tr_loss, tr_acc = run_epoch(X_tr, y_tr, True)
        va_loss, va_acc = run_epoch(X_va, y_va, False)
        print(f"Epoch {epoch:02d} | Tr Loss: {tr_loss:.4f} Acc: {tr_acc:.3f} | Val Loss: {va_loss:.4f} Acc: {va_acc:.3f}")

    os.makedirs(os.path.dirname(CHECKPOINT_PATH), exist_ok=True)
    torch.save(net.state_dict(), CHECKPOINT_PATH)
    print(f"Saved: {CHECKPOINT_PATH}")

if __name__ == "__main__":
    main()
