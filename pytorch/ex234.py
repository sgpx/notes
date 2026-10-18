"""
Write PyTorch code to do an elementwise greater-than comparison between a 2x3 tensor and a 1x3 tensor (using broadcasting), then use the boolean mask to select elements from a third 2x3 tensor.
"""

import torch

a = torch.randint(size=(2,3), low=0, high=10)
b = torch.randint(size=(1,3), low=0, high=10)
c = torch.randint(size=(2,3), low=0, high=10)

mask = a > b
sel = c[mask]
