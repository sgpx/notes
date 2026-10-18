import json
import torch
import torch.optim as optim
import torch.nn as nn

from model import SimpleNN

from torch.utils.data import random_split, TensorDataset, DataLoader


NUM_EPOCHS = 100
BATCH_SIZE = 16
MY_DEVICE = "mps" if torch.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"

with open("target.json","r") as fr:
    raw = fr.read()

rawdict : dict = json.loads(raw)
data = list(rawdict.values())

Xraw, Yraw = [], []

for i in data:
    Xraw.append(i["embedding"])
    Yraw.append(i["is_liked"])


# Convert lists to tensors.
X = torch.tensor(Xraw, dtype=torch.float32).to(device=MY_DEVICE)
Y = torch.tensor(Yraw, dtype=torch.float32).to(device=MY_DEVICE)

# If the model outputs shape [batch_size, 1], make labels match it.
if Y.ndim == 1:
    Y = Y.unsqueeze(1)

orig_dataset = TensorDataset(X, Y)

train_dataset, test_dataset = random_split(dataset=orig_dataset, lengths=[0.8, 0.2])
train_loader = torch.utils.data.DataLoader(train_dataset, shuffle=True, batch_size=BATCH_SIZE)
test_loader = torch.utils.data.DataLoader(test_dataset, shuffle=False, batch_size=BATCH_SIZE)

model = SimpleNN().to(device=MY_DEVICE)

criterion = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)


for epoch in range(NUM_EPOCHS):
    print(f"epoch {epoch} of {NUM_EPOCHS}")
    for X_batch, Y_batch in train_loader:
            optimizer.zero_grad()
            Y_hat = model(X_batch)
            loss = criterion(Y_hat, Y_batch)
            loss.backward()
            optimizer.step()

with torch.no_grad():
    for x_batch, y_batch in test_loader:
        y_hat = model(x_batch)
        loss = criterion(y_hat, y_batch)
        print("inference loss:", loss.item())

torch.save(model.state_dict(), "ex297.pth")