"""

98. `x = torch.zeros(3, 1, 4, 1)`; Result of `x.squeeze().shape`? (Watch out for multiple 1s)
99. `x = torch.zeros(10, 20)`; Result of `x.t().unsqueeze(0)`?
100. `x = torch.zeros(2, 2)`; Result of `torch.cat([x, x], dim=0)`?

"""

import torch


x = torch.randint(size=(3,1,4,1), low=0, high=10)
print(x, x.shape)
y = x.squeeze()
print(y, y.shape)


