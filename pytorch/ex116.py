"""
37. `x = torch.zeros(3, 20)`; Result of `x.view(3, 4, 5)`?
38. `x = torch.zeros(2, 5)`; Result of `x.reshape(5, 2)`?
39. `x = torch.zeros(2, 5)`; Result of `x.reshape(10)`?
40. `x = torch.zeros(1, 1)`; Result of `x.view(1)`?
"""

import torch

a = torch.zeros(3, 20)
b = a.view(3, 4, 5)

print(a, a.shape)
print(b, b.shape)
