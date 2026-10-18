"""
make a (3, 4) random tensor, apply torch.softmax(x, dim=1), and print the row sums. Confirm they're all 1 with torch.allclose.
"""

import torch

x = torch.randint(size=(3,4), low=-10, high=10, dtype=torch.float32)
x = torch.softmax(x, dim=1)
rowsum = torch.sum(x, dim=1)
print(x, rowsum)
print(torch.allclose(torch.ones(3), rowsum))
