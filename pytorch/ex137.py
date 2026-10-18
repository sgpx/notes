"""
59. `x = torch.zeros(1, 1, 1)`; Result of `x.flatten()`?
60. `x = torch.zeros(6, 4)`; Result of `x.flatten(0, 0)`? (Trick: flattening one dim)
"""

import torch

a = torch.zeros(2,3,4,5)
print(a, a.shape)

b = a.flatten(1,-1)
print(b, b.shape, 1, -1)

