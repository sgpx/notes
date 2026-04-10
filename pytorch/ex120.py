"""
41. `x = torch.zeros(2, 3, 4)`; Result of `x.flatten()`?
42. `x = torch.zeros(2, 3, 4)`; Result of `x.flatten(start_dim=0)`?
43. `x = torch.zeros(2, 3, 4)`; Result of `x.flatten(start_dim=1)`?
44. `x = torch.zeros(2, 3, 4)`; Result of `x.flatten(start_dim=2)`?
45. `x = torch.zeros(10, 3, 28, 28)`; Result of `x.flatten(start_dim=1)`? (Common CNN pattern)
46. `x = torch.zeros(5, 1, 1)`; Result of `x.flatten()`?
47. `x = torch.zeros(2, 3, 4)`; Result of `x.flatten(0, 1)`? (Flatten dims 0 and 1 only)
48. `x = torch.zeros(2, 3, 4)`; Result of `x.flatten(1, 2)`?
49. `x = torch.zeros(1, 10)`; Result of `x.flatten()`?
50. `x = torch.zeros(8, 8, 3)`; Result of `x.flatten(0, -1)`?
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

a = torch.zeros(2,3,4)
b = a.flatten()

print(a, a.shape)
print(b, b.shape)
