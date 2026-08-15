# For this program

import torch
x = torch.tensor([2.0, 3.0], requires_grad=True)
W = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
b = torch.tensor([1.0, -1.0], requires_grad=True)

y = W @ x + b            # y.shape = (2,)
loss = y.pow(2).sum()    # Scalar loss
loss.backward()

print(x.grad, W.grad, b.grad, y, loss)

"""
For each variable (`x`, `W`, `b`):

1. **What will `x.grad`, `W.grad`, and `b.grad` contain after the backward pass?

Answer: x.grad will contain dL/dx, W.grad will contain dL/dW, b.grad will contain dL/db where L = loss

2. Briefly explain *why* each variable receives those gradients?

Answer: x,W,b contribute to the computation of loss, and therefore Pytorch traces the computation graph back to them
"""
