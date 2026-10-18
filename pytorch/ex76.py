import torch

a = torch.tensor([1])
b = torch.tensor([2])
c = torch.tensor([3])

d = torch.stack((a,b,c), dim=0)
print(d)

d = torch.stack((a,b,c), dim=1)
print(d)
