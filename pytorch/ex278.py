"""
Write PyTorch code to do compute the Moore-Penrose pseudoinverse of a rank-deficient 3x2 tensor and use it to solve x in Ax=b, verifying A @ pinv @ A ≈ A.
"""

import torch
A = torch.rand(3,1)
A = torch.cat([A, 2*A], dim=1)
B = torch.rand(3,1)
A_pinv = torch.pinverse(A)
x = A_pinv @ B

prod = A @ A_pinv @ A

print(torch.allclose(prod, A))
