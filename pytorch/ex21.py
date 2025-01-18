import torch

x = torch.randint(1,10,(5,))
print(x)

x = torch.clamp(x, 2,7)
print(x)
