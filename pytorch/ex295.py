"""
Write PyTorch code to do: create a 2x3 tensor with finite values and some +inf entries, then use torch.isposinf to replace every positive infinity with the mean of the finite elements.
"""

import torch
a = torch.tensor([[1,2,torch.inf],[3,4,torch.inf]], dtype=torch.float32)
mask = torch.isfinite(a)
fmean = torch.mean(a[mask])
res = torch.where(torch.isposinf(a), fmean, a)
print(res)
