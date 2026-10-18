import torch

tensor_3x3 = torch.rand(3,3)

mean = tensor_3x3.mean()

print(mean.item())

help(mean.item)
