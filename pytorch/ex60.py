import torch

mps = torch.device("mps")
a = torch.rand(5,1)
b = torch.rand(5,1)

a = a.to(mps)
b = b.to(mps)

a += b

print(a, a.device)
