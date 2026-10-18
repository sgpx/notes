import torch

a = torch.ones(1)
print(a)

b = torch.ones(2,2)
print(b)

c = torch.ones(3,3,3, dtype=torch.float64)
print(c)


d = torch.ones(1000,1000,device="mps")
print(d)

