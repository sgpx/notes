"""
19. `x = torch.zeros(2, 2)`; Result of `x.unsqueeze(0).unsqueeze(0)`?
20. `x = torch.zeros(1, 1, 1, 1)`; Result of `x.squeeze()`?
"""

import torch

a = torch.zeros(2,2)
b = a.squeeze(0)
c = b.unsqueeze(0)


print(a, a.shape)
print(b, b.shape)
print(c, c.shape)
