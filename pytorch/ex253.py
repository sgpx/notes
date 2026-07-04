"""
Write a PyTorch script that creates a (3,1) tensor X with tracking enabled, broadcasts it against a (1,4) tensor Y, sums the result, and computes the gradient dX/dLoss
"""

import torch
	
X,Y = torch.randn(3,1, requires_grad=True), torch.randn(1,4, requires_grad=False)
(X+Y).sum().backward()
print(X.grad)

