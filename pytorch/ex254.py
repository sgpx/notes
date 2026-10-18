"""
Write an exact 4-line PyTorch script that manually initializes a batch of inputs X of shape (8,5), a weight matrix W of shape (5,3) with tracking enabled, computes a manual linear layer forward pass (matrix multiplication) to a scalar loss, and updates W manually using standard SGD (subtracting the gradient multiplied by a learning rate of 0.01) inside a context that disables tracking for the update.
"""

import torch

X, W = torch.randn(8, 5), torch.randn(5, 3, requires_grad=True)
(X @ W).sum().backward()

with torch.no_grad():
    W -= (0.01) * W.grad
