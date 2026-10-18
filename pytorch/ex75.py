import torch

a = torch.tensor([1,2])
b = torch.tensor([3,4])

result = torch.stack((a,b), dim=0)
print(result)

result = torch.stack((a,b), dim=1)
print(result)
