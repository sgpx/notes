import torch

x = torch.zeros(1, 5, 10)
print(x)
print(x.squeeze(0), x.shape)
print(x.squeeze(1), x.shape)
print(x.squeeze(), x.shape)
