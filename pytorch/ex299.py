"""
Write PyTorch code to do elementwise inverse hyperbolic tangent on a tensor of values in (-1, 1) using `torch.arctanh`, preserving the input shape.
"""

import torch

x = -1 + (torch.rand(10)* 2)

y = torch.arctanh(x)

print(x,y)
