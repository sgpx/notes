import torch

a = torch.rand(6,4)
b = a.view(2,3,4)

print(a,b)
