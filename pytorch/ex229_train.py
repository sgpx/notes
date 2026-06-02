import os
import torch
from torch.utils.data import DataLoader, random_split, Dataset, WeightedRandomSampler
import torch.nn as nn
import torch.optim as optim
import datetime

from ex226_constants import (
    device_name,
    CHAR_LIM,
    CHAR_TO_IX,
    VOCAB_SIZE,
    input_data_fn,
    model_fn,
)
from ex226_model import FNN

BATCH_SIZE = 150
LOAD_EXISTING_MODEL = True

def encode_char(ch):
    vec = [0] * VOCAB_SIZE
    ix = CHAR_TO_IX.get(ch.lower())
    if ix is not None:
        vec[ix] = 1
    return vec

def process_chunk_to_tensors(chunk):
    z = []
    uarr = []
    for j in chunk:
        uarr.append(1.0 if j.isupper() else 0.0)
        z.extend(encode_char(j))

    pad_chars = CHAR_LIM - len(chunk)
    if pad_chars > 0:
        z.extend([0] * (pad_chars * VOCAB_SIZE))
        uarr = uarr + ([0.0] * pad_chars)

    # Convert to tensors directly
    return torch.tensor(z, dtype=torch.float32), torch.tensor(uarr, dtype=torch.float32)

class TextDataset(Dataset):
    def __init__(self, filepath):
        print("Reading file and creating chunks...", ts())
        self.chunks = []
        self.total_ones = 0
        
        buffer = ""
        with open(filepath, "r", encoding="utf-8", errors="ignore") as fr:
            for line in fr:
                buffer += line + "\n"
                while len(buffer) >= CHAR_LIM:
                    chunk = buffer[:CHAR_LIM]
                    buffer = buffer[CHAR_LIM:]
                    self.chunks.append(chunk)
                    self.total_ones += sum(1 for c in chunk if c.isupper())
                    
        if buffer:
            self.chunks.append(buffer)
            self.total_ones += sum(1 for c in buffer if c.isupper())
            
        self.total_zeros = len(self.chunks) * CHAR_LIM - self.total_ones
        print(f"Created {len(self.chunks)} chunks.", ts())

    def __len__(self):
        return len(self.chunks)

    def __getitem__(self, idx):
        return process_chunk_to_tensors(self.chunks[idx])

ts = lambda: datetime.datetime.now().strftime("%H:%M:%S")

def main():
    print("Starting data preprocessing", ts())
    dataset = TextDataset(input_data_fn)
    print("Completed data preprocessing", ts())

    test_size = int(0.2 * len(dataset))
    train_size = len(dataset) - test_size

    print("creating split", ts())
    train_dataset, test_dataset = random_split(dataset, [train_size, test_size])
    print("created split", ts())

    print("calculating sample weights", ts())
    sample_weights = []
    for idx in train_dataset.indices:
        chunk = dataset.chunks[idx]
        # Weight chunks with more uppercase characters higher, add 1.0 so purely lowercase chunks can still be sampled
        weight = sum(1 for c in chunk if c.isupper()) + 1.0
        sample_weights.append(weight)
        
    sampler = WeightedRandomSampler(
        weights=sample_weights,
        num_samples=len(sample_weights),
        replacement=True
    )
    print("calculated sample weights", ts())

    print("creating loaders", ts())
    # Each sample is already a 4096-character sequence, so keep the minibatch small
    # to avoid exploding the GRU's activation memory on CUDA.
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, sampler=sampler)
    print("created loaders", ts())

    model = FNN().to(device_name)
    if LOAD_EXISTING_MODEL:
        if os.path.exists(model_fn):
            model.load_state_dict(torch.load(model_fn, map_location=device_name))
            print(f"Loaded existing model weights from {model_fn}")
        else:
            print(f"No existing weights found at {model_fn}, starting fresh.")
    
    weight_val = dataset.total_zeros / (dataset.total_ones + 1e-8)
    criterion = nn.BCEWithLogitsLoss(pos_weight=torch.tensor([weight_val], device=device_name))
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    NUM_EPOCHS = 100
    print("Starting training epochs", ts())
    for epoch in range(NUM_EPOCHS):
        print("epoch", epoch)
        model.train()
        for x_batch, y_batch in train_loader:
            x_batch = x_batch.to(device_name)
            y_batch = y_batch.to(device_name)
            
            y_hat = model(x_batch)
            loss = criterion(y_hat, y_batch)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    torch.save(model.state_dict(), model_fn)

    with torch.no_grad():
        model.eval()

        tp = 0
        fp = 0
        fn = 0

        for x, y in test_loader:
            x = x.to(device_name)
            y = y.to(device_name)
            
            pred = model(x)
            pred = (pred > 0.0).float()

            tp += ((pred == 1) & (y == 1)).sum().item()
            fp += ((pred == 1) & (y == 0)).sum().item()
            fn += ((pred == 0) & (y == 1)).sum().item()

        precision = tp / (tp + fp + 1e-8)
        recall = tp / (tp + fn + 1e-8)
        f1 = 2 * precision * recall / (precision + recall + 1e-8)

        print("precision:", precision)
        print("recall:", recall)
        print("f1:", f1)

if __name__ == "__main__":
    main()
