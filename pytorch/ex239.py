"""
"Write PyTorch code to do the elementwise logical NOT of a boolean tensor x, returning a boolean tensor."
"""

import torch
a = torch.tensor([0,1,1,0], dtype=torch.bool)
b = torch.logical_not(a)
print(a,b)
