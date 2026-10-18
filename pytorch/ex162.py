"""
99. `x = torch.zeros(10, 20)`; Result of `x.t().unsqueeze(0)`?
100. `x = torch.zeros(2, 2)`; Result of `torch.cat([x, x], dim=0)`?
"""

import torch

a = torch.zeros(3,1,4,1)
b = a.squeeze()

print(a, a.shape)
print(b, b.shape)
#print(c, c.shape)
