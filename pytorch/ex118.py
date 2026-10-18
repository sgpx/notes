import torch

a = torch.zeros(1,1)
b = a.view(1)

print(a, a.shape)
print(b, b.shape)
