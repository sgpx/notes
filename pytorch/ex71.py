import torch

t = torch.randn(1,3,1,4)
print(t, t.shape)

r = t.squeeze(0)
print(r, r.shape)
