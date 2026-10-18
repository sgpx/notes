import torch

x = torch.tensor(9, dtype=torch.float64)
x.requires_grad_()

y = x**2
y.backward()

print(x.grad)
