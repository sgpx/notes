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

x = torch.arange(1,4, dtype=torch.float32, requires_grad=False)
print(x)
x.requires_grad_()
print(x)

y = x.pow(2) + (3*x)
for i in range(5):

	loss = y.sum()
	loss.backward()
	print(x.grad)
	x.grad.zero_()
