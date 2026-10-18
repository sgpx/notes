"""

95. `x = torch.zeros(5)`; Result of `x.unsqueeze(0).unsqueeze(2)`?
96. `x = torch.zeros(1, 10, 1)`; Result of `x.squeeze().view(2, 5)`?
97. `x = torch.zeros(2, 4)`; Result of `x.view(8).view(2, 2, 2)`?
98. `x = torch.zeros(3, 1, 4, 1)`; Result of `x.squeeze().shape`? (Watch out for multiple 1s)
99. `x = torch.zeros(10, 20)`; Result of `x.t().unsqueeze(0)`?
100. `x = torch.zeros(2, 2)`; Result of `torch.cat([x, x], dim=0)`?

"""

import torch


x = torch.randint(size=(5,), low=0, high=10) # shape = [5]
print(x, x.shape)
y = x.unsqueeze(0) # creates new dimension at dim=0, shape = [1,5]
print(y, y.shape)
y = x.unsqueeze(0).unsqueeze(2) # creates new dimension at dim=2, shape = [1,5,1]
print(y, y.shape)

