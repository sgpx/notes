import torch

a = 100*torch.rand(2,2)
print(a, a.shape)

b = a.unsqueeze(0)
print(b, b.shape)

c = a.unsqueeze(1)
print(c, c.shape)
