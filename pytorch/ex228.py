"""
Write PyTorch code to do: given x of shape (B, C, H, W), permute to (B, H*W, C), z‑score each channel per sample, chunk the batch into 4 parts, apply the same nn.Linear(C, C) to the last dim, and recombine back to (B, C, H, W) without explicit Python loops.
"""

import torch

[b,c,h,w] = list(torch.randint(size=(4,), low=1, high=10))
print(b,c,h,w)

x = torch.randint(low=1, high=10, size=(b,c,h,w))
y = x.permute(0,2,3,1)
y = y.reshape(b,h*w, c)
print(y)

mean = y.mean(dim=1, keepdim=True)
std = y.std(dim=1, keepdim=True, unbiased=False)
std_adj = std + 1e-05 # to prevent divide by zero
y = (y - mean) / (std_adj)

z = torch.chunk(y, chunks=4, dim=0)
linear = torch.nn.Linear(c, c)


z_cat = torch.cat(z, dim=0)
y_lin = linear(z_cat)


y_new = y_lin.reshape(b,h,w,c)
output = y_new.permute(0,3,1,2)
