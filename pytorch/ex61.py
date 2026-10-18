import torch

a = torch.rand(5,1)
a = a.to("mps").to(torch.bfloat16)

print(a, a.device)
