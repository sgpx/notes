import torch

metal = torch.device("mps")

a = torch.randn(5,5)

b = a.to(metal)

print(a.device)
print(b.device)
