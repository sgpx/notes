import sys
import torch

# -----------------------
# Load TorchScript model
# -----------------------
device = "cuda" if torch.cuda.is_available() else "cpu"

model = torch.jit.load("model.pt", map_location=device)
model.eval()


# -----------------------
# Encoding (must match training)
# -----------------------
def encode_chunk(chunk: str):
    chunk = chunk[:4096]

    if len(chunk) < 4096:
        chunk += " " * (4096 - len(chunk))

    vec = torch.tensor(
        [min(ord(c), 255) / 255.0 for c in chunk],
        dtype=torch.float32,
        device=device
    )

    return vec


# -----------------------
# Read input file
# -----------------------
path = sys.argv[-1]

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()


# -----------------------
# Chunk text
# -----------------------
chunks = [
    text[i:i+4096]
    for i in range(0, len(text), 4096)
]

if len(chunks) == 0:
    print("Empty file")
    sys.exit(0)


# -----------------------
# Inference
# -----------------------
votes = []

with torch.no_grad():
    for chunk in chunks:
        x = encode_chunk(chunk)
        x = x.unsqueeze(0)  # batch dimension

        logits = model(x)
        pred = torch.argmax(logits, dim=1).item()

        votes.append(pred)


# -----------------------
# Aggregate result
# -----------------------
py_votes = sum(votes)
nonpy_votes = len(votes) - py_votes

final = "PYTHON" if py_votes > nonpy_votes else "NON-PYTHON"
confidence = max(py_votes, nonpy_votes) / len(votes)

print("File:", path)
print("Chunks:", len(votes))
print("Prediction:", final)
print("Confidence:", round(confidence, 4))