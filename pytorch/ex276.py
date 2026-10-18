"""
Write PyTorch code to do an element-wise bitwise left shift of an integer tensor by another integer tensor (e.g., tensor([3,1,4]) by tensor([1,2,0])) using torch.bitwise_left_shift.
"""

import torch
a = torch.tensor([3,1,4])
b = torch.tensor([1,2,0])
c = torch.bitwise_left_shift(a, b)
print(c)
