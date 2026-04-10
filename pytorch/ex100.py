"""
18. `x = torch.zeros(4, 4, 1)`; Result of `x.squeeze(-1)`?
19. `x = torch.zeros(2, 2)`; Result of `x.unsqueeze(0).unsqueeze(0)`?
20. `x = torch.zeros(1, 1, 1, 1)`; Result of `x.squeeze()`?
"""

import torch

a = torch.zeros(4,4,1)
b = a.squeeze(-1)

print(a, a.shape)
print(b, b.shape)
