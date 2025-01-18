import torch

t = torch.arange(5)
mask = t > 2

ee = t[mask]

print(t, mask, ee)
