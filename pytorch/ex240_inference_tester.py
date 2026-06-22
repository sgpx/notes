#!/usr/bin/env python3
import torch
import numpy as np
import os

# Import your classes/functions from a3.py
from a3 import UsefulClassifier, load_embedding_vector

def test_inference_pipeline():
    print("Running inference test...")
    
    # 1. Setup Mock Dimensions
    embed_dim = 768  # Standard for ViT-L/14
    batch_size = 1
    
    # 2. Instantiate Model
    model = UsefulClassifier(embed_dim=embed_dim)
    model.eval()
    
    # 3. Create dummy data
    # Create random vectors to simulate CLIP embeddings
    mock_ref = torch.randn(batch_size, embed_dim)
    mock_frame = torch.randn(batch_size, embed_dim)
    
    # 4. Run Forward Pass
    with torch.no_grad():
        logits = model(mock_ref, mock_frame)
    
    # 5. Validate output shape
    assert logits.shape == (batch_size, 2), f"Expected shape (1, 2), got {logits.shape}"
    print("Inference test passed: Model output shape is correct.")
    
    # 6. Test Softmax conversion
    probs = torch.softmax(logits, dim=1)
    print(f"Probabilities: Not Useful: {probs[0][0]:.2%}, Useful: {probs[0][1]:.2%}")

def test_path_loading():
    print("\nRunning path loading test...")
    # This assumes your DB exists. Replace with a real path if needed.
    DB_PATH = "embeddings.db"
    if not os.path.exists(DB_PATH):
        print("Skipping path loading test: DB not found.")
        return

    import sqlite3
    conn = sqlite3.connect(DB_PATH)
    
    # Try to grab one row to verify functionality
    cursor = conn.execute("SELECT path FROM embeddings LIMIT 1")
    row = cursor.fetchone()
    
    if row:
        path_to_test = row[0]
        vec = load_embedding_vector(conn, path_to_test)
        assert vec is not None, "Failed to load vector for existing path."
        print(f"Path loading test passed: Loaded vector of size {vec.shape} for {path_to_test}")
    else:
        print("Database is empty.")
    
    conn.close()

if __name__ == "__main__":
    test_inference_pipeline()
    test_path_loading()
