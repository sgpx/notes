import torch
from ex226_constants import CHAR_TO_IX, CHAR_LIM, VOCAB_SIZE, device_name, model_fn
from ex226_model import FNN


def encode_char(ch):
    vec = [0] * VOCAB_SIZE
    ix = CHAR_TO_IX.get(ch.lower())
    if ix is not None:
        vec[ix] = 1
    return vec

def encode(text):
    encoded = []

    for ch in text[:CHAR_LIM]:
        encoded.extend(encode_char(ch))

    while len(encoded) < CHAR_LIM * VOCAB_SIZE:
        encoded.append(0)

    return torch.tensor(encoded, dtype=torch.float32).unsqueeze(0).to(device_name)


def apply_caps(original, pred, threshold=0.5):
    out = []

    for i, ch in enumerate(original[:CHAR_LIM]):
        if pred[i] > threshold:
            out.append(ch.upper())
        else:
            out.append(ch.lower())

    return "".join(out)


# load model
model = FNN().to(device_name)
model.load_state_dict(torch.load(model_fn, map_location=device_name))
model.eval()


while True:
    s = input(">>> ")

    if not s.strip():
        continue

    with torch.no_grad():
        x = encode(s)
        y_hat = torch.sigmoid(model(x)).squeeze(0).cpu().numpy()
        print(y_hat)

    result = apply_caps(s, y_hat)

    print("capitalized:", result)
