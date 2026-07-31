"""
For a tensor x, write code to do a logical AND of x > 0 and x % 2 == 0 using torch.logical_and
"""

import torch
x = torch.randint(low=0,high=10, size=(5,))
mask = torch.logical_and((x > 0),(x % 2 == 0))
print(x, mask, x[mask])
