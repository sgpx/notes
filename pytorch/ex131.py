"""
51. `x = torch.zeros(2, 2, 2, 2)`; Result of `x.flatten(2, 3)`?
52. `x = torch.zeros(2, 2, 2, 2)`; Result of `x.flatten(0, 2)`?
53. `x = torch.zeros(5)`; Result of `x.flatten()`?
54. `x = torch.zeros(1, 5)`; Result of `x.flatten(0)`?
55. `x = torch.zeros(3, 1, 3)`; Result of `x.flatten(1)`?
56. `x = torch.zeros(10, 20, 30)`; Result of `x.flatten(start_dim=0, end_dim=1)`?
57. `x = torch.zeros(10, 20, 30)`; Result of `x.flatten(start_dim=1, end_dim=2)`?
58. `x = torch.zeros(2, 3, 4, 5)`; Result of `x.flatten(1, -1)`?
59. `x = torch.zeros(1, 1, 1)`; Result of `x.flatten()`?
60. `x = torch.zeros(6, 4)`; Result of `x.flatten(0, 0)`? (Trick: flattening one dim)
"""

import torch

a = torch.zeros(2,2,2,2)
print(a, a.shape)

b = a.flatten(0)
print(b, b.shape, 0)

b = a.flatten(1)
print(b, b.shape, 1)

b = a.flatten(1, 1)
print(b, b.shape, 1,1)

b = a.flatten(2)
print(b, b.shape, 2)

b = a.flatten(2, 3)
print(b, b.shape, 2, 3)

b = a.flatten(0, 2)
print(b, b.shape, 0, 2)
