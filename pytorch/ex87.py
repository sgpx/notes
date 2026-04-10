import torch

x = torch.zeros(1, 5, 10)
y = x.squeeze()
print(x, x.shape)
print(y, y.shape)

