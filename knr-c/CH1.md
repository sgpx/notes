"""
Problem 2 — Autograd: simple gradients
Goal: Learn how PyTorch computes gradients with autograd.
What to do
- Create a tensor x with requires_grad=True, for example x = torch.tensor([1.0, -2.0, 3.0], requires_grad=True).
- Define y = x.pow(2) + 3*x (element-wise operations).
- Compute a scalar loss as y.sum(), then call loss.backward().
- Print x.grad to see dy/dx for each element.
Hints
- Remember to call .sum() before backward so you have a scalar loss.
- Gradients are for dy/dx w.r.t x.
What to submit
- The values in x.grad.
"""

import torch

x = torch.randint(low=1, high=10,size=(3,),dtype=torch.float32)
x.requires_grad_()

y = x.pow(2) + (3*x)

z = y.sum()
z.backward()

print(x, y, z)
print(x.grad)
