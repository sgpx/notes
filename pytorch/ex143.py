"""
72. `x = torch.zeros(2, 3, 4)`; Result of `x.transpose(0, 2)`?
73. `x = torch.zeros(1, 2, 1)`; Result of `x.permute(1, 0, 2)`?
74. `x = torch.zeros(3, 4, 5)`; Result of `x.permute(0, 1, 2)`?
75. `x = torch.zeros(3, 2)`; Result of `x.transpose(-1, -2)`?
76. `x = torch.zeros(2, 3, 4, 5)`; Result of `x.transpose(1, 3)`?
77. `x = torch.zeros(1, 2, 3)`; Result of `x.permute(2, 0, 1)`?
78. `x = torch.zeros(5, 1)`; Result of `x.T`?
79. `x = torch.zeros(4, 4)`; Result of `x.permute(1, 0)`?
80. `x = torch.zeros(2, 1, 2)`; Result of `x.transpose(0, 1)`?
"""

import torch

a = torch.zeros(2,3,4)
b = a.transpose(0,2)

print(a, a.shape)
print(b, b.shape)
