"""
Problem 3 — Clearing gradients and a tiny function
Goal: Practice reusing gradients by zeroing and computing again.
What to do
- Use the same x from Problem 2 (or redefine it) with requires_grad=True.
- Define z = x * x + 2*x + 1, and compute loss_z = z.sum(), then backward and print x.grad.
- Now reset gradients with x.grad.zero_(), redefine z2 = x * x * x (x cubed) and compute loss_z2 = z2.sum(), backward, and print
x.grad again.
Hints
- You can reuse the same x or redefine; zeroing is important if you want to do multiple backward passes in one run.
What to submit
- Gradients after the first backward pass, and after the second backward pass (separate prints).
"""

import torch

x = torch.randint(low=1, high=10,size=(3,),dtype=torch.float32)
x.requires_grad_()

y = x.pow(2) + (3*x)

z = y.sum()
z.backward()

print(x, y, z)
print(x.grad)
x.grad.zero_()

z = x * x + 2*x + 1
loss_z = z.sum()

loss_z.backward()
print(x.grad)
x.grad.zero_()


z = x ** 3
loss_z = z.sum()

loss_z.backward()
print(x.grad)
x.grad.zero_()

