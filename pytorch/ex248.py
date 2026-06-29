"""
Write PyTorch code to do expand a 1x3 tensor to match the shape of a 4x3 tensor using torch.expand_as.
"""

import torch

a = torch.randint(size=(1,3), low=0, high=10)
b = torch.randint(size=(4,3), low=0, high=10)

c = a.expand_as(b) # creates view of `a` to be memory efficient
print(c) 
