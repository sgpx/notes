import torch
import numpy

metal = torch.device("mps")

a = torch.rand((10**5,10**3), device=metal)
b = torch.rand((10**5,10**3), device=metal)

c = a+b


print(c)
