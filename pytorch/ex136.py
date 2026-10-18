"""
57. `x = torch.zeros(10, 20, 30)`; Result of `x.flatten(start_dim=1, end_dim=2)`?
58. `x = torch.zeros(2, 3, 4, 5)`; Result of `x.flatten(1, -1)`?
59. `x = torch.zeros(1, 1, 1)`; Result of `x.flatten()`?
60. `x = torch.zeros(6, 4)`; Result of `x.flatten(0, 0)`? (Trick: flattening one dim)
"""

import torch

a = torch.zeros(10,20,30)
print(a, a.shape)

b = a.flatten(1,2)
print(b, b.shape, 1,2)

