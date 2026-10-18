"""
Write PyTorch code to replace values > 0.5 in a (3, 4) tensor with -1 using torch.masked_fill.
"""

import torch
a = torch.randn(3,4)
mask = a>0.5
b = a.masked_fill(mask, -1)
print(b)
