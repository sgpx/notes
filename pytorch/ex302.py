"""
Write PyTorch code to compute the vector norm of each row in a 2D tensor using `torch.linalg.vector_norm`, so a tensor of shape `(4, 6)` becomes a 1D tensor of shape `(4,)` with the norm taken over the last dimension.
"""

import torch
a = torch.rand(4,6)
b = torch.linalg.vector_norm(a, dim=1)

print(a,b)

