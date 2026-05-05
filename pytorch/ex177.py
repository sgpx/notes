"""
Assuming you want Problem 5 rewritten as a single, self-contained atomic programming task (concise spec + expected outputs), here it is:

Task — Mini-batch linear regression (single atomic problem)
- Goal: Train a linear model y = w0*x0 + w1*x1 + b using mini-batch SGD with PyTorch tensors and autograd.
- Data: Create 8 samples with a known linear relation (use float32):
  - X: shape (8,2). Example rows (you may use these):
    [[0.5, 1.0],
     [1.0, 0.0],
     [1.5, 2.0],
     [2.0, 1.0],
     [2.5, 3.0],
     [3.0, 0.5],
     [3.5, 2.5],
     [4.0, 1.5]]
  - y: shape (8,) computed from y = 1.5*x0 + (-2.0)*x1 + 0.5 (compute as floats).
- Model parameters: Initialize W as a tensor shape (2,) and b as shape (1,) with requires_grad=True (random init).
- Data pipeline: Wrap X,y in torch.utils.data.TensorDataset and use DataLoader with batch_size=2 and shuffle=True.
- Training loop:
  - Set lr = 0.01, epochs = 3.
  - For each epoch:
    - For each batch (xb, yb) from the loader:
      - y_hat = xb.matmul(W) + b
      - loss = ((y_hat - yb)**2).mean()
      - loss.backward()
      - with torch.no_grad(): W -= lr * W.grad; b -= lr * b.grad
      - zero gradients: W.grad.zero_(); b.grad.zero_()
    - After finishing all batches, compute and print the epoch loss on the full dataset (mean squared error).
- Submit:
  - The printed loss value for each epoch (3 numbers).
  - Two example pairs of (predicted, true) from the final model on two sample inputs.
"""

import torch

a = torch.randn(size=(8,1))
b = [[i[0], 1] for i in a]
print(b)

for n,i in range(len(b)):
	if n > 0:
		x0 = b[n-1][0]
		x1 = b[n][0]
		y = 1.5*x0 + (-2.0)*x1 + 0.5 
		b[n][1] = y


