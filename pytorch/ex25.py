import torch

mean = 0
stdev = 1
a = torch.normal(mean, stdev, size=(10,))
print(a)
print(a.std())
