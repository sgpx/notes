"""
60. `x = torch.zeros(6, 4)`; Result of `x.flatten(0, 0)`? (Trick: flattening one dim)
"""

import torch

a = torch.zeros(6,4)
print(a, a.shape)

b = a.flatten(0,0)
print(b, b.shape, 0,0)

