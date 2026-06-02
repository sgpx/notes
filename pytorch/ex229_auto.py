import os
import torch
import torch.nn as nn
import torch.optim as optim
import json
import shutil
import llm

from ex226_constants import (
    device_name,
    CHAR_LIM,
    CHAR_TO_IX,
    VOCAB_SIZE,
    model_fn,
)
from ex226_model import FNN

# Import our new modules
from ex226_eval import evaluate_model, collect_failures
from ex226_failure import llm_classify
from ex226_memory import update_failures, get_failure_stats
from ex226_prompt import build_prompts

# Hardcoded flags/hyperparameters
TARGET_F1 = 0.90
MAX_LOOPS = 50
BATCH_SIZE = 5
LR = 0.001
OUTPUT_FILE = "dataset-ex226-auto.txt"
CHECKPOINT_FILE = "ex226_auto_checkpoint.json"
OPTIMIZER_FILE = "ex226_optimizer.pth"
BEST_MODEL_FILE = "best_model-ex226.pth"
TOLERANCE = 0.05

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

def generate_synthetic_data(prompts):
    generated_texts = []
    for i, prompt in enumerate(prompts):
        print(f"Generating item {i+1}/{len(prompts)}...")
        try:
            res = llm.invoke(prompt)
            if res:
                generated_texts.append(res)
                with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                    f.write(res + "\n")
        except Exception as e:
            print(f"Error invoking LLM: {e}")
    return generated_texts

def train_on_data(model, optimizer, texts):
    if not texts:
        return 0.0
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
    return loss.item()

def main():
    print("Starting zero-touch autonomous AutoML training...")
    
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
        except Exception as e:
            pass
            
    # Evaluate initial score if starting fresh loop
    precision, recall, f1 = evaluate_model(model)
    best_score = f1
    print(f"Initial Eval F1: {best_score:.4f}")
    
    for loop in range(start_loop, MAX_LOOPS + 1):
        print(f"\n--- Loop {loop}/{MAX_LOOPS} ---")
        
        # 1. Diagnose
        failures = collect_failures(model)
        print(f"Found {len(failures)} failures in eval set.")
        
        categories = llm_classify(failures)
        if categories:
            print(f"LLM extracted failure categories: {categories}")
            update_failures(categories)
            
        # 2. Adapt
        stats = get_failure_stats()
        prompts = build_prompts(stats, BATCH_SIZE)
        
        # 3. Generate
        print("Generating targeted synthetic data using LLM...")
        new_data = generate_synthetic_data(prompts)
        
        if not new_data:
            print("Failed to generate texts (LLM might be down). Exiting loop.")
            break
            
        # 4. Retrain
        loss = train_on_data(model, optimizer, new_data)
        print(f"Training loss on new batch: {loss:.4f}")
        
        # 5. Evaluate
        _, _, new_f1 = evaluate_model(model)
        print(f"New Eval F1: {new_f1:.4f}")
        
        # 6. Rollback / Promote
        if new_f1 < best_score - TOLERANCE:
            print(f"Catastrophic drift detected! ({new_f1:.4f} < {best_score:.4f} - {TOLERANCE}). Rolling back.")
            if os.path.exists(BEST_MODEL_FILE):
                model.load_state_dict(torch.load(BEST_MODEL_FILE, map_location=device_name))
        else:
            print("Promoting checkpoint...")
            if new_f1 > best_score:
                best_score = new_f1
            torch.save(model.state_dict(), BEST_MODEL_FILE)
            
        torch.save(model.state_dict(), model_fn)
        torch.save(optimizer.state_dict(), OPTIMIZER_FILE)
        
        with open(CHECKPOINT_FILE, "w") as f:
            json.dump({"next_loop": loop + 1}, f)
            
        if best_score >= TARGET_F1:
            print(f"Reached decent best F1 score ({best_score:.4f} >= {TARGET_F1}). Stopping autonomous loop.")
            break
            
    print("Autonomous unsupervised loop finished.")

if __name__ == "__main__":
    main()
