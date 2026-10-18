import torch

x = torch.zeros(1,1,5)
y = x.squeeze()

print(x, x.shape)
print(y, y.shape)
