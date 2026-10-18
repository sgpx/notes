import torch

x = torch.zeros(1, 5, 10)
y = x.squeeze(0)
print(x, x.shape)
print(y, y.shape)

