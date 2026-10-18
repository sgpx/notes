"""
Create a 5x5 random matrix and use torch.trace to compute the sum of its diagonal elements. Confirm the result by extracting the diagonal with torch.diag and summing it with torch.sum
"""

import torch

a = torch.rand(5,5)

diagsum = torch.trace(a)

print(diagsum)

d2 = torch.sum(torch.diag(a))

print(torch.allclose(d2, diagsum))
