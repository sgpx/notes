"""
Initialize a 3x3 tensor with requires_grad=True, multiply all elements by 10, and compute the sum. Call .backward() on the result, print the gradients, and then manually clear them using .grad.zero_().
"""

import torch

a = torch.rand(3,3, requires_grad=True)
print(a)

y = torch.sum(a * 10)
print(y)
y.backward()
print(a.grad)

a.grad.zero_()
print(a.grad)
