"""

92. `x = torch.zeros(2, 5)`; Result of `x[..., None].shape`?
93. `x = torch.zeros(3, 3)`; Result of `x.view(1, 3, 3).repeat(2, 1, 1)`?
94. `x = torch.zeros(2, 3, 4)`; Result of `x.transpose(1, 2).contiguous().view(2, 12)`?
95. `x = torch.zeros(5)`; Result of `x.unsqueeze(0).unsqueeze(2)`?
96. `x = torch.zeros(1, 10, 1)`; Result of `x.squeeze().view(2, 5)`?
97. `x = torch.zeros(2, 4)`; Result of `x.view(8).view(2, 2, 2)`?
98. `x = torch.zeros(3, 1, 4, 1)`; Result of `x.squeeze().shape`? (Watch out for multiple 1s)
99. `x = torch.zeros(10, 20)`; Result of `x.t().unsqueeze(0)`?
100. `x = torch.zeros(2, 2)`; Result of `torch.cat([x, x], dim=0)`?

"""

import torch

x = torch.randint(size=(3,3), low=0, high=10)
print(x, x.shape)
print(x[...,None], x[...,None].shape)

# adds a new dimension at the end after all preceeding dimensions
# it is similar to x.unsqueeze(-1)
