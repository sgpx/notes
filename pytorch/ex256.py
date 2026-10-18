"""
Math (SVD Foundations): Given the symmetric matrix A=[
3 2
2 3
], find its eigenvalues lambda_1, lambda_2. Because A is symmetric and positive-definite, its singular values sigma_i are simply the absolute values of its eigenvalues (sigma_i = |lambda_i|). Calculate lambda_1, lambda_2 

Write an exact 3-line PyTorch script that creates your exact 2*2 tensor A from the math problem above, passes it into torch.linalg.svd(), and prints just the singular values vector S.
"""

import torch

a = torch.tensor([[3,2],[2,3]], dtype=torch.float32)
print(torch.linalg.svd(a).S)

