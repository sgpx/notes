"""
Write PyTorch code to replace each element in a tensor with its sign using `torch.sign`, so negative values become -1, zeros become 0, and positive values become 1.
"""

import torch

a = torch.randint(low=-5, high=5, size=(10,))
b = torch.sign(a)

print(a,b)
