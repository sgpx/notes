from model import SimpleNN
import gpt as llm
import torch
from sys import argv
input_str = argv[-1]

MY_DEVICE = "mps" if torch.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"

emb = llm.get_embedding(input_str)
emb_tensor = torch.Tensor(emb).to(dtype=torch.float32, device=MY_DEVICE)
emb_tensor = emb_tensor.unsqueeze(0)

model = SimpleNN().to(device=MY_DEVICE)

model.load_state_dict(torch.load("ex297.pth", map_location=MY_DEVICE, weights_only=True))
model.eval()

with torch.no_grad():
    Y_hat = model(emb_tensor)
    prob = torch.sigmoid(Y_hat).item()

print(f"Prediction for '{input_str}':")
print(f"Raw logit: {Y_hat.item():.4f}")
print(f"Probability (liked): {prob:.4f}")
print(f"Class: {'Liked' if prob > 0.5 else 'Disliked'}")