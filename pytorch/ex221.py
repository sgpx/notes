"""
Write PyTorch code to do element-wise multiplication of a (3,2) tensor and a (1,2) tensor using torch.mul with broadcasting, storing the output in a pre-allocated tensor.
"""

import torch

a = torch.rand(3,2)
b = torch.rand(1,2)

c = torch.empty(3,2)
torch.mul(a,b,out=c)

print(a,b,c)
