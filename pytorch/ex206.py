"""

91. `x = torch.zeros(2, 5)`; Result of `x[:, None, :].shape`? (Indexing unsqueeze)
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

x = torch.randint(size=(2,5), low=0, high=10)
print(x[:,None,:])
print(x[:,None,:].shape)

"""
This code creates a 2×5 integer tensor then inserts a new dimension between the first and second axes. Step-by-step:

- torch.randint(size=(2,5), low=0, high=10) produces a tensor x with shape (2, 5) — two rows and five columns of random integers in [0,10).
- x[:, None, :] uses advanced indexing to add a new axis at index 1. The slice x[:, None, :] means:
  - : (all) for the first dimension (size 2),
  - None inserts a new dimension of size 1,
  - : (all) for the last dimension (size 5).
- As a result x[:, None, :] has shape (2, 1, 5). Each original row of x becomes a 1×5 slice along the new middle dimension.

Example: if x =
[[a b c d e],
 [f g h i j]]
then x[:, None, :] =
[[[a b c d e]],
 [[f g h i j]]]
and printing .shape shows torch.Size([2, 1, 5]).
"""
