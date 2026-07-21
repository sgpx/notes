# Write a program to compute the Jacobian matrix of the function f(x)=x^3 evaluated at the tensor x=[2.0,3.0] using torch.autograd.functional.jacobian.
import torch

f = lambda X : X**3

x = torch.tensor([2.0, 3.0])

print(torch.autograd.functional.jacobian(f, x))
