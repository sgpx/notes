# Write a PyTorch script to compute the Hessian matrix of f(x,y)=x^2*y+y^3 at x=1,y=2 using torch.autograd.functional.hessian.

import torch

f = lambda z : ((z[0]**2)*z[1]) + (z[1]**3)
inputs = torch.tensor([1.0, 2.0])

res = torch.autograd.functional.hessian(f, inputs)
print(res)
