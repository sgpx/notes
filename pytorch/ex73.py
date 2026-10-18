import torch

a = torch.randint(1,10,(4,))
b = torch.sum(a)
print(b.item())
