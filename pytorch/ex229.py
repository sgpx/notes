# check
# Write PyTorch code to do: given x of shape (B, C, H, W), permute to (B, H*W, C), z‑score each channel per sample, chunk the batch into 4 parts, apply the same nn.Linear(C, C) to the last dim, and recombine back to (B, C, H, W) without explicit Python loops.

import torch

[b,c,h,w] = torch.randint(size=(4,), low=1, high=10).tolist()
print(b,c,h,w)
assert b % 4 == 0

x = torch.randint(low=1, high=10, size=(b,c,h,w), dtype=torch.float32)
y = x.permute(0,2,3,1)
y = y.reshape(b,h*w, c)
print(y)

mean = y.mean(dim=1, keepdim=True)
std = y.std(dim=1, keepdim=True, unbiased=False)
std_adj = std + 1e-05 # to prevent divide by zero
y = (y - mean) / (std_adj)

y_chunks = y.reshape(4, b//4, h*w, c)

linear = torch.nn.Linear(c, c)

y_lin = linear(y_chunks)



y_new = y_lin.reshape(b,h,w,c)
output = y_new.permute(0,3,1,2)
