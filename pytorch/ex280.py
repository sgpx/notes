"""
Write PyTorch code to do the elementwise hyperbolic cosine (torch.cosh) of a tensor x with shape (2, 3) and store the result in y, preserving the input's dtype and device.
"""

import torch
x = torch.rand(2,3, dtype=torch.float32, device="cuda")
y = torch.cosh(x).to(dtype=x.dtype, device=x.device)
