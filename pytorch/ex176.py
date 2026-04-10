"""

Problem 5 — Mini-batch training with DataLoader
Goal: Learn how to use a DataLoader to feed data in batches.
What to do
- Create a small dataset (8 samples) for a simple linear problem:
  X and y e.g. a simple linear relation y = 1.5*x0 + -2.0*x1 + 0.5
- Use torch.utils.data.TensorDataset and torch.utils.data.DataLoader with batch_size=2.
- Use the same manual update rule as Problem 4, but update parameters after each batch.
- Train for a few epochs (e.g., 3) and print the loss every epoch.
Hints
- Build dataset like: dataset = TensorDataset(X, y); loader = DataLoader(dataset, batch_size=2, shuffle=True)
- In the batch loop, compute loss on the batch, backward, and update.
What to submit
- The loss printed after each epoch and a couple of example predicted vs. true values.

"""

import torch
from torch.utils.data import TensorDataset, DataLoader

X = torch.randn(8, 2)
x0 = X[:,0]
x1 = X[:,1]
print(X, x0, x1)
y = 1.5*x0 - 2*x1 + 0.5

W = torch.randint(size=(2,), dtype=torch.float32,requires_grad=True, high=10, low=1)
b = torch.randint(size=(1,), dtype=torch.float32,requires_grad=True, high=10, low=1)

lr = 0.01

dataset = TensorDataset(X, y)

loader = DataLoader(dataset, shuffle=True, batch_size=2)


for i in range(50):
	for X_batch, y_batch in loader:
		y_hat = X_batch.matmul(W) + b
		loss = torch.mean((y_hat - y_batch)**2)
		loss.backward()
	
		with torch.no_grad():
			W -= lr * (W.grad)
			b -= lr * (b.grad)

			W.grad.zero_()
			b.grad.zero_()
		print("loss: ", loss.item())
print("final", W, b, y_hat, y, X)

