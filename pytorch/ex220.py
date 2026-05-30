"""
Write PyTorch code to do argsort on a 2D tensor along dim=1 to obtain indices that sort each row in descending order and use them to reorder each row's elements.
"""

import torch

size=(3,3)

a = torch.randint(size=size, low=0, high=10)
print(a)
indices = a.argsort(dim=1, descending=True)
print(indices)

b = torch.gather(a, dim=1, index=indices)

print(b)
