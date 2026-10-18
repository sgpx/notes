import torch
import numpy as np

a = torch.arange(5)
print(a)
b = torch.tensor(np.arange(5))
print(b)
c = torch.tensor(np.array([[1,2,3],[4,5,6],[5,6,7]]))
print(c)
