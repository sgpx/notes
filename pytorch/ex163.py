"""
100. `x = torch.zeros(2, 2)`; Result of `torch.cat([x, x], dim=0)`?
"""

import torch

a = torch.zeros(2,2)
b = torch.cat([a,a], dim=0)

print(a, a.shape)
print(b, b.shape)
