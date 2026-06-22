import torch

f = lambda x : (3*x**2 + 2*x)
x1 = torch.tensor(4)
dx = torch.tensor(0.0005)

manual_grad = (f(x1+dx) - f(x1))/dx

x_pt = torch.tensor(4, requires_grad=True, dtype=torch.float32)
y = f(x_pt)
y.backward()

print(x_pt.grad.item(), manual_grad.item())
