# Given a tensor with some dimensions of size 1, use tensor.squeeze() to remove those singleton dimensions.

import torch

a = torch.randn(1,3,1)

b = a.squeeze(0)

c = b.squeeze(1)

print(b,b.shape)
print(c,c.shape)
