import sys
import torch

# -----------------------
# Model definition REQUIRED for state_dict
# -----------------------
class FNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU(inplace=True)
        self.fc1 = torch.nn.Linear(4096, 2048)
        self.fc2 = torch.nn.Linear(2048, 1024)
        self.fc3 = torch.nn.Linear(1024, 512)
        self.fc4 = torch.nn.Linear(512, 256)
        self.fc5 = torch.nn.Linear(256, 128)
        self.fc6 = torch.nn.Linear(128, 64)
        self.fc7 = torch.nn.Linear(64, 32)
        self.fc8 = torch.nn.Linear(32, 16)
        self.fc9 = torch.nn.Linear(16, 8)
        self.fc10 = torch.nn.Linear(8, 4)
        self.fc11 = torch.nn.Linear(4, 2)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.relu(self.fc3(x))
        x = self.relu(self.fc4(x))
        x = self.relu(self.fc5(x))
        x = self.relu(self.fc6(x))
        x = self.relu(self.fc7(x))
        x = self.relu(self.fc8(x))
        x = self.relu(self.fc9(x))
        x = self.relu(self.fc10(x))
        return self.fc11(x)


# -----------------------
# Load model
# -----------------------
device = "cuda" if torch.cuda.is_available() else "cpu"

model = FNN().to(device)
model.load_state_dict(torch.load("model.pt", map_location=device))
model.eval()


# -----------------------
# Encoding
# -----------------------
def encode_chunk(chunk):
    chunk = chunk[:4096]
    if len(chunk) < 4096:
        chunk += " " * (4096 - len(chunk))

    return torch.tensor(
        [min(ord(c), 255) / 255.0 for c in chunk],
        dtype=torch.float32,
        device=device
    )


# -----------------------
# File input
# -----------------------
path = sys.argv[-1]

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

chunks = [text[i:i+4096] for i in range(0, len(text), 4096)]

if not chunks:
    print("Empty file")
    sys.exit(0)


# -----------------------
# Inference
# -----------------------
votes = []

with torch.no_grad():
    for chunk in chunks:
        x = encode_chunk(chunk).unsqueeze(0)

        logits = model(x)
        pred = torch.argmax(logits, dim=1).item()

        votes.append(pred)


py_votes = sum(votes)
final = "PYTHON" if py_votes > len(votes) / 2 else "NON-PYTHON"

print("File:", path)
print("Chunks:", len(votes))
print("Prediction:", final)