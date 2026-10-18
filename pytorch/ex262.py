"""
Write PyTorch code to do: create a 2x3 complex tensor with both real and complex entries and use torch.isreal to return a boolean mask of purely real elements.
"""

import torch
r = torch.randint(size=(2,3), low=1, high=11)
i = torch.randint(size=(2,3), low=-1, high=5)

a = r + i*1j
b = torch.isreal(a)
print(a, b, a[b])
