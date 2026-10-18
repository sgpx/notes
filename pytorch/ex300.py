"""
Write PyTorch code to rotate a 2D tensor `x` by 90 degrees counterclockwise using `torch.rot90`, so that a tensor of shape `(3, 4)` becomes `(4, 3)`.
"""

import torch

a = torch.rand(3,4)
b = torch.rot90(a)

print(a.shape, b.shape)
