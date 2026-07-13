"""
Write PyTorch code to do in-place elementwise division of tensor a by scalar 5 using torch.div_.
"""

import torch
a = torch.tensor([1,2,3,4], dtype=torch.float32).div_(5.0)
