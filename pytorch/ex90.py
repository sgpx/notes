"""
5. `x = torch.zeros(10, 1)`; Result of `x.squeeze(0)`? (Trick question: does dim 0 have size 1?)
6. `x = torch.zeros(5, 5)`; Result of `x.unsqueeze(0)`?
7. `x = torch.zeros(5, 5)`; Result of `x.unsqueeze(1)`?
8. `x = torch.zeros(5, 5)`; Result of `x.unsqueeze(-1)`?
9. `x = torch.zeros(2, 3, 4)`; Result of `x.unsqueeze(2)`?
10. `x = torch.zeros(1, 2, 1, 3)`; Result of `x.squeeze()`?
11. `x = torch.zeros(1, 2, 1, 3)`; Result of `x.squeeze(0)`?
12. `x = torch.zeros(1, 2, 1, 3)`; Result of `x.squeeze(2)`?
13. `x = torch.zeros(7)`; Result of `x.unsqueeze(0)`?
"""
import torch

x = torch.zeros(10,1)
y = x.squeeze(0)

print(x, x.shape)
print(y, y.shape)

y = x.squeeze()

print(x, x.shape)
print(y, y.shape)
