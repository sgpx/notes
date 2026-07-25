"""
Write PyTorch code to do create a 3x4 tensor of ones (using torch.ones) with dtype=torch.float32 on the GPU if available, and set requires_grad=True.
"""

import torch

a = torch.ones(3,4, dtype=torch.float32, requires_grad=True)
device = "cuda" if torch.cuda.is_available() else "mps" if torch.mps.is_available() else "cpu"
a = a.to(device)
print(a)
