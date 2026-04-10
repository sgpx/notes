import torch

a = torch.tensor([1,2,4])
print(a.device)

b = a.to("mps")
print(a, b)
