# Given a 1D tensor, add an extra dimension to convert it into a 2D tensor with shape (1, N).

import torch

a = torch.randint(1,10,(5,))
b = a.unsqueeze(0)

print(a,"\n", b)


