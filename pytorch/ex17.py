import torch

a = torch.tensor([[1,2,3],[2,3,4],[4,5,6]])

print(a)
print(torch.transpose(a, 0, 1))
print(torch.transpose(a, 0, 0))
