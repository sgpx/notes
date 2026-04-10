"""
21. `x = torch.zeros(4, 5)`; Result of `x.view(20)`?
"""

import torch

a = torch.zeros(4,5)
b = a.view(20)

print(a, a.shape)
print(b, b.shape)
