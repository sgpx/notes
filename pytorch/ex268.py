# Write a Pytorch program to compute the Hessian matrix for the function f(x,y)=3x^2 +2y^2 given x = 2 and y = 3

import torch

x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

f = 3*x**2 + 2*y**2

grad_x, grad_y = torch.autograd.grad(f, (x,y), create_graph=True, allow_unused=True)
print(grad_x, grad_y)

hxx = torch.autograd.grad(grad_x, x, retain_graph=True, allow_unused=True, create_graph=True)[0]
hxy = torch.autograd.grad(grad_x, y, retain_graph=True, allow_unused=True, create_graph=True)[0]
hyx = torch.autograd.grad(grad_y, x, retain_graph=True, allow_unused=True, create_graph=True)[0]
hyy = torch.autograd.grad(grad_y, y, retain_graph=True, allow_unused=True, create_graph=True)[0]

hxx = hxx if hxx else torch.tensor(0.0, requires_grad=True)
hyx = hyx if hyx else torch.tensor(0.0, requires_grad=True)
hxy = hxy if hxy else torch.tensor(0.0, requires_grad=True)
hyy = hyy if hyy else torch.tensor(0.0, requires_grad=True)

result = torch.tensor([[hxx, hxy],[hyx,hyy]])

print(result)

# use torch.autograd.functional.hessian to verify

from torch.autograd.functional import hessian

F = lambda X,Y : 3*X**2 + 2*Y**2

H = torch.tensor(hessian(F, (x,y)))

print(H)

print(torch.all(torch.isclose(result, H)))
