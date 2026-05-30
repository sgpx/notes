"""
Write PyTorch code to do compute the L2 norm of each row of a 2D tensor and return a column vector (keepdim=True) using torch.norm.
"""

import torch

a = torch.rand(4,4)
print(torch.norm(a, p=2, dim=1, keepdim=True))
