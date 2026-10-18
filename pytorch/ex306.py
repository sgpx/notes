"""
Run nn.Linear(4, 2) on a random input twice, once normally and once inside torch.no_grad(). Print out.requires_grad and out.grad_fn for each.
"""

import torch

model = torch.nn.Linear(4,2)

x = torch.rand(4)
out = model(x)
print(x)
print(out)
print(out.requires_grad)
print(out.grad_fn)
print("===")

with torch.no_grad():
	x = torch.rand(4)
	out = model(x)
	print(x)
	print(out)
	print(out.requires_grad)
	print(out.grad_fn)
