import torch
a = torch.zeros(3, 1, 4)
b = a.squeeze(1)

print(a, a.shape)
print(b, b.shape)
