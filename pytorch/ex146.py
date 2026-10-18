"""
77. `x = torch.zeros(1, 2, 3)`; Result of `x.permute(2, 0, 1)`?
78. `x = torch.zeros(5, 1)`; Result of `x.T`?
79. `x = torch.zeros(4, 4)`; Result of `x.permute(1, 0)`?
80. `x = torch.zeros(2, 1, 2)`; Result of `x.transpose(0, 1)`?
"""

import torch

a = torch.zeros(1,2,3)
b = a.permute(2,0,1)

print(a, a.shape)
print(b, b.shape)
