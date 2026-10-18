"""
Write PyTorch code to do create a 3x4 tensor filled with -2.5 using torch.full with dtype=torch.float32 on CUDA if available.
"""

import torch
a = torch.full((3,4), -2.5, dtype=torch.float32, device="cuda" if torch.cuda.is_available() else "cpu")
print(a)
