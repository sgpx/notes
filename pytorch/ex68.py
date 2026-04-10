import torch

a = torch.tensor([1,2,3])
print(a)
print(a.shape)

b = a.unsqueeze(0)
print(b)
print(b.shape)

c = a.unsqueeze(1)
print(c)
print(c.shape)
