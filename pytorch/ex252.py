"""
Write a PyTorch script that creates a (3,1) tensor X with tracking enabled, broadcasts it against a (1,4) tensor Y, sums the result, and computes the gradient dX/dLoss
"""

import torch
	
X = torch.randn(3,1, dtype=torch.float32, requires_grad=True)
Y = torch.randn(1,4, dtype=torch.float32, requires_grad=True)

res = X + Y
print(res.shape)

loss = res.sum()
loss.backward()
dX_dLoss = X.grad
print(dX_dLoss)
