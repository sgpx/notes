import torch

x = torch.randn(1, 100)
print(x)

print(torch.mean(x))
print(torch.std(x))

x = torch.randn(2, 3)

print(x)

x = torch.randn(2, 2, 2)

print(x)
