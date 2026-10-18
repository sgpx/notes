#!/usr/bin/env python3
import os
import torch
import numpy as np
from PIL import Image
import clip
from a3 import UsefulClassifier, normalize_unit # Reusing your model and utility

# ---------------- Configuration ----------------
TEST_DIR = "./test"
REF_PATH = "./ref.png"
CHECKPOINT_PATH = "checkpoints/useful_classifier_mlp.pt"
MODEL_NAME = "ViT-L/14"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def main():
    # 1. Load CLIP for embeddings
    model, preprocess = clip.load(MODEL_NAME, device=DEVICE)
    model.eval()

    # 2. Prepare Reference Embedding
    with torch.no_grad():
        ref_img = Image.open(REF_PATH).convert("RGB")
        ref_in = preprocess(ref_img).unsqueeze(0).to(DEVICE)
        ref_emb = model.encode_image(ref_in).float().cpu().numpy()
    ref_emb = normalize_unit(ref_emb) # [1, D]

    # 3. Load Trained Classifier
    # Assuming embed_dim is 768 for ViT-L/14
    net = UsefulClassifier(embed_dim=768).to(DEVICE)
    net.load_state_dict(torch.load(CHECKPOINT_PATH, map_location=DEVICE))
    net.eval()

    # 4. Inference loop
    test_files = [os.path.join(TEST_DIR, f) for f in os.listdir(TEST_DIR) 
                  if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

    print(f"Running inference on {len(test_files)} images...")
    
    with torch.no_grad():
        for p in test_files:
            # Process frame
            img = Image.open(p).convert("RGB")
            img_in = preprocess(img).unsqueeze(0).to(DEVICE)
            frame_emb = model.encode_image(img_in).float().cpu().numpy()
            frame_emb = normalize_unit(frame_emb) # [1, D]

            # Convert to tensors
            r_tensor = torch.tensor(ref_emb, dtype=torch.float32, device=DEVICE)
            f_tensor = torch.tensor(frame_emb, dtype=torch.float32, device=DEVICE)

            # Classify
            logits = net(r_tensor, f_tensor)
            probs = torch.softmax(logits, dim=1)
            prediction = logits.argmax(dim=1).item()

            label = "USEFUL" if prediction == 1 else "NOT_USEFUL"
            print(f"{os.path.basename(p)}: {label} (Conf: {probs[0][prediction]:.2%})")
            if label == "NOT_USEFUL":
                try: os.remove(os.path.abspath(p))
                except Exception as e: print(e)

if __name__ == "__main__":
    main()
