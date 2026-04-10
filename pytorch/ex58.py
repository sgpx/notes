import torch

a = torch.tensor([1.2,3.4], dtype=torch.float64)

b = a.to(torch.int32)

print(a)
print(b)
