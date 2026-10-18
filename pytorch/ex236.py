"""
Write PyTorch code to do an LU decomposition of a square tensor using torch.lu and torch.lu_unpack to extract L, U, and the permutation P, then reconstruct the original tensor and verify equality.
"""

import torch

A = torch.randn(3,3, dtype=torch.float32)
print(A)
LU, pivots = torch.lu(A)
print(LU, pivots)
P,L,U = torch.lu_unpack(LU, pivots)
print(P, L, U)
A_reconstructed = P @ L @ U
print(A_reconstructed)
assert torch.allclose(A, A_reconstructed, atol=1e-6)
print("reconstruction OK")

