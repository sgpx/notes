import torch

a = torch.tensor([[2,1],[1,2]])
print(a.shape)

flat = a.view(-1)
print(flat)
print(flat.shape)
