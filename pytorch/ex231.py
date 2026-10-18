"""
Write PyTorch code to do raise each 3x3 matrix in a batched tensor A (shape [B,3,3]) to the k-th power using torch.linalg.matrix_power.
"""

import torch
B = 5
A = torch.randn(B,3,3)
k = 3
result = torch.linalg.matrix_power(A, k)
