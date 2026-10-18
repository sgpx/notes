import torch
import random

x = torch.tensor([1,2,3])
print(x)

y = torch.tensor([[1,2],[3,4]])
print(y)

z = torch.tensor([[ [1], [2] ], [ [3], [4] ]])
print(z)

a = torch.tensor([1,2,3], dtype=torch.int32)
b = torch.tensor([4,5,6], dtype=torch.int64)

print(a.dtype, b.dtype)

import torch

c = torch.tensor([random.randint(1,100) for i in range(10000000)], device="mps")
d = torch.tensor([random.randint(1,100) for i in range(10000000)], device="mps")

print(torch.sum(c+d))
print(torch.sum(c*d))
