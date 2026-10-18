"""
Write PyTorch code to do compute the 25th, 50th, and 75th nanquantiles along dim=1 of a 2D tensor, ignoring NaNs and keeping the output dimension (keepdim=True) using torch.nanquantile.
"""

import torch

a = torch.rand(100,100,dtype=torch.float32)
q25 = torch.nanquantile(a, torch.tensor(0.25), interpolation='nearest', dim=1, keepdim=True)
q50 = torch.nanquantile(a, torch.tensor(0.5), interpolation='nearest', dim=1, keepdim=True)
q75 = torch.nanquantile(a, torch.tensor(0.75), interpolation='nearest', dim=1, keepdim=True)

print(a, q25, q50, q75)

