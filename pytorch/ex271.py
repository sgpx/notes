# Write a PyTorch script to compute the Hessian matrix of f(x,y)=x^2*y+y^3 at x=1,y=2 using torch.autograd.functional.hessian.

import torch

f = lambda x,y : ((x**2)*y) + (y**3)
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(2.0, requires_grad=True)

res = torch.autograd.functional.hessian(f, (x,y))

print(res)
