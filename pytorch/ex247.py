"""
Problem:

Write PyTorch code to do: given a batch of square matrices A and matching batch RHS B, compute LU with torch.lu and solve AX = B with torch.lu_solve, then verify solutions with torch.allclose.
"""

import torch

A = torch.randint(size=(10,2,2), low=1, high=10).to(dtype=torch.float32)
B = torch.randint(size=(10,2,1), low=1, high=10).to(dtype=torch.float32)

LU, pivots = torch.lu(A)
X = torch.lu_solve(B, LU, pivots)
prod = torch.matmul(A, X)
print(torch.allclose(prod, B, rtol=1e-4, atol=1e-6))
