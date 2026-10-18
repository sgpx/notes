import sys
import torch

# -----------------------
# Device
# -----------------------
device = "cuda" if torch.cuda.is_available() else "cpu"

# -----------------------
# Load TorchScript model (NO CLASS NEEDED)
# -----------------------
model = torch.jit.load("model.pt", map_location=device)
model.eval()


# -----------------------
# Encoding function
# -----------------------
def encode_chunk(chunk: str):
    chunk = chunk[:4096]
    chunk = chunk.ljust(4096)

    x = torch.tensor(
        [min(ord(c), 255) / 255.0 for c in chunk],
        dtype=torch.float32,
        device=device
    )

    return x


# -----------------------
# Read input file
# -----------------------
path = sys.argv[1]

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

chunks = [text[i:i+4096] for i in range(0, len(text), 4096)]

if len(chunks) == 0:
    print("Empty file")
    sys.exit(0)


# -----------------------
# Inference
# -----------------------
votes = []

with torch.no_grad():
    for chunk in chunks:
        x = encode_chunk(chunk).unsqueeze(0)  # (1, 4096)

        logits = model(x)
        pred = torch.argmax(logits, dim=1).item()

        votes.append(pred)


# -----------------------
# Majority vote
# -----------------------
py_votes = sum(votes)
final = "PYTHON" if py_votes > len(votes) / 2 else "NON-PYTHON"


# -----------------------
# Output
# -----------------------
print("File:", path)
print("Chunks:", len(votes))
print("Prediction:", final)