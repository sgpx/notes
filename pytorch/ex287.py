"""
Write PyTorch code to do a QR decomposition using torch.qr on a given (4, 3) tensor x, returning Q of shape (4, 3) with orthonormal columns and R of shape (3, 3) upper-triangular such that x = Q @ R.
"""

import torch
x = torch.randint(low=1, high=10, size=(4,3), dtype=torch.float32)
Q,R = torch.qr(x)
print(Q)
print(R)
