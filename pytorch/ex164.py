"""
Goal: Create a tensor, inspect its properties, and do a few simple operations.
What to do
- Create a 3x2 tensor with numbers 1 through 6.
- Print its shape, dtype, and device.
- Multiply the tensor by 2, sum all elements, and take the maximum value.
Hints
- Use torch.arange and .reshape or .view to shape it.
- Use .shape, .dtype, and .device to inspect.
What to submit
- The printed shape, dtype, device, the result of the sum, and the max value.
"""

import torch

a = torch.arange(1,7, dtype=torch.float32).reshape(3,2)
print(a.shape, a.dtype, a.device)

print(a)

c = a * 2
print(c)
b = torch.sum(c)
print(b.item())

print(torch.max(a))
