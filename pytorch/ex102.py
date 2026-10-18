"""
20. `x = torch.zeros(1, 1, 1, 1)`; Result of `x.squeeze()`?
"""

import torch

a = torch.zeros(1, 1, 1, 1)
b = a.squeeze()

print(a, a.shape)
print(b, b.shape)
