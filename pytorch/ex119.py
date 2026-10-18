import torch

a = torch.zeros(2,5)
b = a.view(10)

print(a, a.shape)
print(b, b.shape)
