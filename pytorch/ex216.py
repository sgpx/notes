"""

100. `x = torch.zeros(2, 2)`; Result of `torch.cat([x, x], dim=0)`?

"""

import torch


x = torch.randint(size=(2,2), low=0, high=10)
print(x, x.shape)
y = torch.cat([x,x], dim=1)
print(y, y.shape)

