"""
topic torch.lt: "Write PyTorch code to do an elementwise less-than comparison between a (3,4) tensor and a scalar using torch.lt, then use the boolean mask to set all elements >= scalar to zero in-place."
"""

import torch
a = torch.rand(3,4)
b = ~torch.lt(a, 0.1)
a[b] = 0
