import glob
import torch
import torch.nn as nn
import torch.optim as optim
from PIL import Image
from model import LetterCNN, build_preprocess_transform

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print("Using", device)
allfiles = glob.glob("*.png")
preprocess = build_preprocess_transform()

Xf = []
Yf = []

for fpath in allfiles:
    img = Image.open(fpath).convert("RGB")
    img_tensor = preprocess(img).unsqueeze(0).to(device)
    Xf.append(img_tensor)

X = torch.cat(Xf, dim=0).to(device)
Yf = torch.tensor([1 if "-true" in fpath else 0 for fpath in allfiles], dtype=torch.float32)
Y = Yf.view(-1, 1).to(device)


dataset = torch.utils.data.TensorDataset(X, Y)
test_len = int(0.2 * len(allfiles))
train_len = len(allfiles) - test_len

train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_len, test_len])

train_loader = torch.utils.data.DataLoader(train_dataset, shuffle=True, batch_size=32)
test_loader = torch.utils.data.DataLoader(test_dataset, shuffle=False, batch_size=32)
model = LetterCNN()
model = model.to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

NUM_EPOCHS = 100

model.train()

for epoch in range(NUM_EPOCHS):
    print("epoch", epoch)
    epoch_loss = 0
    ctr = 0
    for x_batch, y_batch in train_loader:
        ctr += 1
        y_hat = model(x_batch)
        optimizer.zero_grad()
        loss = criterion(y_hat, y_batch)
        epoch_loss += loss.item()
        loss.backward()
        optimizer.step()

    print("epoch loss:", epoch_loss / ctr)


model.eval()

with torch.no_grad():
    for x_batch, y_batch in test_loader:
        y_hat = model(x_batch)
        loss = criterion(y_hat, y_batch)
        print("inference loss:", loss.item())

torch.save(model.state_dict(), "model-ex288.pth")
