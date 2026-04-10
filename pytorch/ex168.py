import torch

a = torch.tensor([1,2], dtype=torch.float32)
a.requires_grad_()
b = a**2
print(b)
c = b.sum()
c.backward()
print(c)
print(a,b,c)
print(a.grad)
