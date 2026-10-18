"""
Create a 4x4 random float tensor, apply torch.sign to determine the polarity of each element, and use a boolean mask to extract only the strictly positive values into a new 1D tensor.
"""

import torch

a = torch.rand(4,4)
b = torch.sign(a)
mask = b > 0
c = a[mask]

print(c)
