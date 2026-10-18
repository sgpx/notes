"""
write a LSTM to approximate pi to the Nth digit with K layers, if N and K are constants
"""
import torch
import torch.nn as nn
import torch.optim as optim
import mpmath as mp

#N_DIGITS = 1_000_000
N_DIGITS = 1_000_0

def save_pi_digits(max_digits, filename="pi_digits.txt", chunk_size=1000):
    # Set the precision context once
    mp.mp.dps = max_digits
    
    print("Computing pi... (This stays in RAM temporarily)")
    pi_str = mp.nstr(mp.mp.pi, max_digits)
    
    print(f"Streaming digits to {filename} in chunks...")
    # Open file and stream in chunks to keep memory usage at zero during write
    with open(filename, "w") as f:
        for i in range(0, len(pi_str), chunk_size):
            f.write(pi_str[i:i+chunk_size])
            
    print("Done! Memory cleared.")

def load_pi_digits():
    with open("pi_digits.txt","r") as f: return f.read()

save_pi_digits(N_DIGITS)


class MyLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MyLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, x):
        output, _ = self.lstm(x)
        x = output[:, -1, :]
        x = self.relu(x)
        x = self.fc(x)
        return x

model = MyLSTM(input_size=1, hidden_size=128, output_size=1).to(device="mps")
mseloss = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

pi_digits = load_pi_digits()

seq_len = 10
num_seq = len(pi_digits) - seq_len + 1

X = torch.zeros((num_seq, seq_len, 1))
X = X.to(device="mps")
Y = torch.zeros((num_seq, 1))
Y = Y.to(device="mps")

for i in range(num_seq):
    if i + seq_len >= N_DIGITS + 3: break 
    window = pi_digits[i:i+seq_len]
    X[i] = torch.tensor([float(c) if c != "." else 0 for c in window], dtype=torch.float32).unsqueeze(-1)
    target_digit = pi_digits[i+seq_len]
    Y[i] = torch.tensor(float(target_digit), dtype=torch.float32)


NUM_EPOCHS = 100

for i in range(NUM_EPOCHS):
    pred = model(X)
    loss = mseloss(pred, Y)
    print(i, loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


"""
Great question! Let me break down what's happening in that data preparation loop.

## The Window and Target Digit Explained

**The `window`** is a **sequence of consecutive digits from pi** that the LSTM will learn from. In your example with `seq_len = 10`, if pi starts as `3.14159265358979...`, the first window would be the first 10 digits: `"3141592653"`.

**The `target_digit`** is **the next digit immediately after that window**—the one the model is trying to predict. So for the first window `"3141592653"`, the target would be `"5"` (the 11th digit).

This creates a **sequence-to-single-value prediction task**: "Given these 10 digits, predict the next one."

---

## Why Individual Digits as Input?

You're passing individual digits because **the LSTM processes sequences one timestep at a time**. Here's how it works:

| Timestep | Input | What the LSTM sees |
|----------|-------|-------------------|
| t=0 | `[1]` | First digit: 1 |
| t=1 | `[4]` | Second digit: 4 |
| t=2 | `[2]` | Third digit: 2 |
| t=3 | `[7]` | Fourth digit: 7 |
| t=4 | `[8]` | Fifth digit: 8 |
| t=5 | `[5]` | Sixth digit: 5 |

The LSTM maintains hidden state as it processes each digit sequentially. By the end, it's absorbed the pattern from all 6 digits and makes a prediction about what comes next.

### Why unsqueeze(-1)?

```python
X[i] = torch.tensor([float(c) for c in window], dtype=torch.float32).unsqueeze(-1)
```

- `[float(c) for c in window]` creates a 1D list: `[1.0, 4.0, 2.0, 7.0, 8.0, 5.0]`
- `.unsqueeze(-1)` adds a dimension: `[[1.0], [4.0], [2.0], [7.0], [8.0], [5.0]]`

This reshapes it from shape `(10,)` to shape `(10, 1)` because your LSTM expects `(sequence_length, input_size)`, where `input_size=1` (one feature per timestep—the digit itself).

---

## The Training Loop

For each position `i` in the pi digits:
1. Extract digits at positions `[i, i+seq_len)` as the input sequence
2. Extract the digit at position `i+seq_len` as the target
3. Feed the sequence in, and the model predicts what that target digit should be

Does this clarify the mechanism?
"""
