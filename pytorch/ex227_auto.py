import os
import torch
import torch.nn as nn
import torch.optim as optim
import json

from ex226_constants import (
    device_name,
    CHAR_LIM,
    CHAR_TO_IX,
    VOCAB_SIZE,
    model_fn,
)
from ex226_model import FNN
from ex226_gen import generate_synthetic_data_batch

# Hardcoded flags/hyperparameters
TARGET_F1 = 0.90
MAX_LOOPS = 50
BATCH_SIZE = 5
LR = 0.001
OUTPUT_FILE = "dataset-ex226-auto.txt"
CHECKPOINT_FILE = "ex226_auto_checkpoint.json"
OPTIMIZER_FILE = "ex226_optimizer.pth"

def encode_char(ch):
    vec = [0] * VOCAB_SIZE
    ix = CHAR_TO_IX.get(ch.lower())
    if ix is not None:
        vec[ix] = 1
    return vec

def process_text_to_tensors(text):
    z = []
    uarr = []
    
    chunk = text[:CHAR_LIM]
    
    for j in chunk:
        uarr.append(1 if j.isupper() else 0)
        z.extend(encode_char(j))

    pad_chars = CHAR_LIM - len(chunk)
    if pad_chars > 0:
        z.extend([0] * (pad_chars * VOCAB_SIZE))
        uarr = uarr + ([0] * pad_chars)

    return z, uarr

def main():
    print(f"Starting autonomous unsupervised GAN-like training...")
    print(f"Target F1: {TARGET_F1}, Max Loops: {MAX_LOOPS}, Batch Size: {BATCH_SIZE}")
    
    model = FNN().to(device_name)
    if os.path.exists(model_fn):
        model.load_state_dict(torch.load(model_fn, map_location=device_name))
        print(f"Loaded existing model weights from {model_fn}")
    else:
        print(f"No existing weights found at {model_fn}, starting fresh.")
        
    optimizer = optim.Adam(model.parameters(), lr=LR)
    if os.path.exists(OPTIMIZER_FILE):
        try:
            optimizer.load_state_dict(torch.load(OPTIMIZER_FILE, map_location=device_name))
            print(f"Loaded optimizer state from {OPTIMIZER_FILE}")
        except Exception as e:
            print(f"Could not load optimizer state: {e}")
            
    start_loop = 1
    if os.path.exists(CHECKPOINT_FILE):
        try:
            with open(CHECKPOINT_FILE, "r") as f:
                state = json.load(f)
                start_loop = state.get("next_loop", 1)
                print(f"Resuming from LLM loop {start_loop}...")
        except Exception as e:
            print(f"Could not read checkpoint file: {e}")
    
    for loop in range(start_loop, MAX_LOOPS + 1):
        print(f"\n--- Loop {loop}/{MAX_LOOPS} ---")
        
        print("Generating synthetic data using LLM...")
        texts = generate_synthetic_data_batch(BATCH_SIZE, output_file=OUTPUT_FILE)
        
        if not texts:
            print("Failed to generate texts (LLM might be down). Exiting loop.")
            break
            
        allX = []
        allY = []
        
        for text in texts:
            z, uarr = process_text_to_tensors(text)
            allX.append(z)
            allY.append(uarr)
            
        tX = torch.tensor(allX, dtype=torch.float32, device=device_name)
        tY = torch.tensor(allY, dtype=torch.float32, device=device_name)
        
        total_ones = sum(sum(y) for y in allY)
        total_zeros = (len(allY) * CHAR_LIM) - total_ones
        weight_val = total_zeros / (total_ones + 1e-8)
        criterion = nn.BCEWithLogitsLoss(pos_weight=torch.tensor([weight_val], device=device_name))
        
        model.train()
        y_hat = model(tX)
        loss = criterion(y_hat, tY)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        model.eval()
        with torch.no_grad():
            pred = (y_hat > 0.0).float()
            
            tp = ((pred == 1) & (tY == 1)).sum().item()
            fp = ((pred == 1) & (tY == 0)).sum().item()
            fn = ((pred == 0) & (tY == 1)).sum().item()
            
            precision = tp / (tp + fp + 1e-8)
            recall = tp / (tp + fn + 1e-8)
            f1 = 2 * precision * recall / (precision + recall + 1e-8)
            
        print(f"Loss: {loss.item():.4f}")
        print(f"Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}")
        
        torch.save(model.state_dict(), model_fn)
        torch.save(optimizer.state_dict(), OPTIMIZER_FILE)
        try:
            with open(CHECKPOINT_FILE, "w") as f:
                json.dump({"next_loop": loop + 1}, f)
        except Exception as e:
            print(f"Could not write checkpoint: {e}")
        print(f"Updated and saved gradients to {model_fn} and checkpointed loop {loop}.")
        
        if f1 >= TARGET_F1:
            print(f"Reached decent F1 score ({f1:.4f} >= {TARGET_F1}). Stopping autonomous loop.")
            break
            
    print("Autonomous unsupervised loop finished.")

if __name__ == "__main__":
    main()
