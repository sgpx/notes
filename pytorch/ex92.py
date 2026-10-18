"""
9. `x = torch.zeros(2, 3, 4)`; Result of `x.unsqueeze(2)`?
10. `x = torch.zeros(1, 2, 1, 3)`; Result of `x.squeeze()`?
11. `x = torch.zeros(1, 2, 1, 3)`; Result of `x.squeeze(0)`?
12. `x = torch.zeros(1, 2, 1, 3)`; Result of `x.squeeze(2)`?
13. `x = torch.zeros(7)`; Result of `x.unsqueeze(0)`?
"""

import torch

x = torch.zeros(2,3,4)
y = x.unsqueeze(2)

print(x, x.shape)
print(y, y.shape)
