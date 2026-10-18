"""
Write PyTorch code to do: create a tensor with finite values, -inf, +inf and NaN, use torch.isposinf to find positive infinities and replace them with the tensor's maximum finite value.
"""

import torch
a = [1,2,3,4,-float("inf"),float("inf")]
b = torch.tensor(a, dtype=torch.float32)
fin = b[torch.isfinite(b)]
c = torch.where(torch.isposinf(b), torch.max(fin), b)
