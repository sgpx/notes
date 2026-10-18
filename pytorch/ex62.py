import torch
import numpy as np

a = torch.arange(1,6)
b = a.numpy()


print(a)
print(b)
print(np.mean(b))
