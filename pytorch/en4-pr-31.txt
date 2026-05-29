Here's a simple, concrete learning problem that you can solve using PyTorch and a custom Dataset (torch.utils.data.Dataset).

Problem
- Goal: Learn to predict y from x where y ≈ 3x + 2 with some Gaussian noise.
- Why this is easy: a small neural net or even linear regression should easily fit it; it’s a single-feature regression problem.

What you’ll implement
- A custom Dataset that generates synthetic (x, y) pairs on the fly.
- A tiny training loop using a DataLoader to batch data.
- A simple model (e.g., a single linear layer) to learn the relationship.

Code (all-in-one example)

```python
import torch
from torch.utils.data import Dataset, DataLoader

# 1) Easy synthetic dataset: y = 3*x + 2 + noise
class SimpleLinearDataset(Dataset):
    def __init__(self, n_samples=1000, noise_std=0.1, seed=42):
        super().__init__()
        self.n_samples = n_samples
        self.noise_std = noise_std
        g = torch.Generator().manual_seed(seed)

        # x in [0, 1)
        self.x = torch.rand(n_samples, 1, generator=g)
        # y = 3*x + 2 + Gaussian noise
        self.y = 3.0 * self.x + 2.0 + torch.randn(n_samples, 1, generator=g) * noise_std

    def __len__(self):
        return self.n_samples

    def __getitem__(self, idx):
        # Return a tuple (x, y) for the given index
        return self.x[idx], self.y[idx]

# 2) Simple training setup
def train():
    # Create dataset and data loader
    dataset = SimpleLinearDataset(n_samples=2000, noise_std=0.1, seed=123)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    # Model: a tiny linear regressor (1 input feature, 1 output)
    model = torch.nn.Linear(1, 1)

    # Loss and optimizer
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    # Train for a few epochs
    epochs = 50
    for epoch in range(epochs):
        epoch_loss = 0.0
        for xb, yb in dataloader:
            pred = model(xb)
            loss = criterion(pred, yb)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item() * xb.size(0)

        avg_loss = epoch_loss / len(dataset)
        if (epoch + 1) % 10 == 0 or epoch == 0:
            print(f"Epoch {epoch+1}/{epochs}, Loss: {avg_loss:.6f}")

    # Inspect learned parameters
    with torch.no_grad():
        w = model.weight.item()
        b = model.bias.item()
        print(f"Learned parameters: weight ≈ {w:.3f}, bias ≈ {b:.3f}")
        print("Expected: weight ≈ 3.0, bias ≈ 2.0")

if __name__ == "__main__":
    train()
```

What you’ll see
- The model should converge toward weight ≈ 3.0 and bias ≈ 2.0.
- This demonstrates how to build a custom Dataset, feed it to a DataLoader, and train a simple model.

How to extend
- Change the problem: generate x in a different range and modify y = a*x + b + noise, and see if the model learns a and b.
- Increase complexity: use x with more features (e.g., x is 2D, y = w1*x1 + w2*x2 + b) and a slightly more capable model (e.g., a small neural network).
- Use the dataset with non-linear relationships by using y = sin(2πx) + noise and a small MLP.
