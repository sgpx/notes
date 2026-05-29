"""

99. `x = torch.zeros(10, 20)`; Result of `x.t().unsqueeze(0)`?
100. `x = torch.zeros(2, 2)`; Result of `torch.cat([x, x], dim=0)`?

"""

import torch


x = torch.randint(size=(10,20), low=0, high=10)
print(x, x.shape)
y = x.t()
print(y, y.shape)
y = x.t().unsqueeze(0)
print(y, y.shape)


