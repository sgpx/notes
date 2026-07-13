"""
Write PyTorch code to do the elementwise base-10 logarithm of a tensor using torch.log10, adding a small epsilon to zeros to avoid -inf.
"""

import torch
t = torch.rand(5,5, dtype=torch.float32)
eps = 1e-06
t = torch.where(t == 0, t + eps, t)
print(torch.log10(t))
