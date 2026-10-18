"""
24. `x = torch.zeros(4, 5)`; Result of `x.view(-1)`?
25. `x = torch.zeros(4, 5)`; Result of `x.view(2, -1)`?
26. `x = torch.zeros(4, 5)`; Result of `x.view(-1, 2)`?
27. `x = torch.zeros(2, 3, 4)`; Result of `x.view(6, 4)`?
28. `x = torch.zeros(2, 3, 4)`; Result of `x.view(2, 12)`?
29. `x = torch.zeros(1, 10)`; Result of `x.view(10)`?
30. `x = torch.zeros(1, 10)`; Result of `x.view(10, 1)`?
31. `x = torch.zeros(2, 2, 2)`; Result of `x.view(8)`?
32. `x = torch.zeros(10, 2)`; Result of `x.view(5, 4)`?
33. `x = torch.zeros(12)`; Result of `x.view(3, 2, 2)`?
34. `x = torch.zeros(12)`; Result of `x.view(3, -1, 2)`?
35. `x = torch.zeros(100)`; Result of `x.view(1, 10, 10)`?
36. `x = torch.zeros(100)`; Result of `x.view(10, 1, 10)`?
37. `x = torch.zeros(3, 20)`; Result of `x.view(3, 4, 5)`?
38. `x = torch.zeros(2, 5)`; Result of `x.reshape(5, 2)`?
39. `x = torch.zeros(2, 5)`; Result of `x.reshape(10)`?
40. `x = torch.zeros(1, 1)`; Result of `x.view(1)`?
"""

import torch

a = torch.zeros(4,5)
b = a.view(-1)

print(a, a.shape)
print(b, b.shape)
