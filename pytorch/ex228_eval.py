import torch
from ex226_constants import CHAR_LIM, VOCAB_SIZE, CHAR_TO_IX, device_name

eval_samples = [
    "I met John Smith in London.",
    "NASA launched a rocket.",
    "She said, 'Hello world!'",
    "The CEO of IBM is arriving.",
    "Mr. Dr. Prof. edge case.",
    "Is it Dr. Smith or Prof. Jones?",
    "It's a beautiful day in New York City.",
    "Wait, you mean the FBI?",
    "Alice and Bob went to Paris, France.",
    "Welcome to the United States of America."
]

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

def apply_caps(original, pred, threshold=0.0):
    out = []
    for i, ch in enumerate(original[:CHAR_LIM]):
        if pred[i] > threshold:
            out.append(ch.upper())
        else:
            out.append(ch.lower())
    return "".join(out)

def evaluate_model(model):
    model.eval()
    tp, fp, fn = 0, 0, 0
    with torch.no_grad():
        for text in eval_samples:
            x = encode(text)
            y_hat = model(x).squeeze(0)
            pred = (y_hat > 0.0).float()
            
            y_arr = [1.0 if c.isupper() else 0.0 for c in text[:CHAR_LIM]]
            while len(y_arr) < CHAR_LIM:
                y_arr.append(0.0)
            y = torch.tensor(y_arr, device=device_name)
            
            tp += ((pred == 1) & (y == 1)).sum().item()
            fp += ((pred == 1) & (y == 0)).sum().item()
            fn += ((pred == 0) & (y == 1)).sum().item()
            
    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)
    return precision, recall, f1

def collect_failures(model):
    model.eval()
    failures = []
    with torch.no_grad():
        for text in eval_samples:
            x = encode(text)
            y_hat = model(x).squeeze(0).cpu().numpy()
            
            pred_text = apply_caps(text, y_hat)
            if pred_text != text:
                failures.append({
                    "gold": text,
                    "pred": pred_text
                })
    return failures
