import torch
x = torch.randn(5, requires_grad=True, dtype=torch.float32)
y = torch.expm1(x)
mask = (y > 0).to(y.dtype)
y_pos = y * mask
out = y_pos.clone()
loss = out.sum()
loss.backward()
print(x)
print(y)
print(mask)
print(out)
print(x.grad)
