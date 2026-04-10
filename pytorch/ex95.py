"""
13. `x = torch.zeros(7)`; Result of `x.unsqueeze(0)`?
"""

import torch

x = torch.zeros(7)
y = x.unsqueeze(0)

print(x, x.shape)
print(y, y.shape)

