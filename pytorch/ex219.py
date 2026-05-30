"""
write code using type_as to convert tensor b to the data type and device of tensor a
"""
import torch

a = torch.randint(size=(5,5), low=0, high=11, device="mps", dtype=torch.float32)
print(a)

b = torch.randint(size=(5,5), low=0, high=11, device="cpu", dtype=torch.int8)
print(b)

b = b.type_as(a)

print(b)
