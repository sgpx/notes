"""
Write PyTorch code to do create a 3x3 float tensor of ones directly on CUDA if available (otherwise on CPU) and print the tensor.device.
"""

import torch

a = torch.ones(3,3, device="cuda" if torch.cuda.is_available() else "cpu")
print(a.device)
