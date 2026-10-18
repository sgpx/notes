import torch

x = torch.zeros(7)
y = x.unsqueeze(1)

print(x, x.shape)
print(y, y.shape)

