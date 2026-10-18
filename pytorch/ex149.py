"""
80. `x = torch.zeros(2, 1, 2)`; Result of `x.transpose(0, 1)`?
"""

import torch

a = torch.zeros(2,1,2)
b = a.transpose(0,1)

print(a, a.shape)
print(b, b.shape)
