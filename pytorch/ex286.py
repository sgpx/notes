"""
Write PyTorch code to flip a 3×4 tensor vertically (reverse the order of its rows) using torch.flipud.
"""

import torch
a = torch.rand(3,4)
print(a.flipud())

