"""
Problem 4 — A tiny linear regression by hand (no nn.Module)
Goal: Do a simple learning task with manual parameters using autograd.
What to do
- Create a tiny dataset X of shape (3, 2) and y of shape (3,).
  Example:
  X = [[1.0, 2.0],
       [2.0, 0.5],
       [3.0, 1.0]]
  y = [5.0, 4.0, 6.0]
- Initialize W with shape (2,) and b with shape (1,), both with requires_grad=True.
- Forward: y_hat = X.matmul(W) + b
- Loss: mean squared error between y_hat and y
- Backprop: loss.backward()
- Update: with torch.no_grad(), do W -= lr * W.grad and b -= lr * b.grad, then zero the gradients.
- Repeat for a few iterations (e.g., 50) with a small learning rate (e.g., 0.01).
Hints
- Use X.matmul(W) for matrix-vector multiplication; shapes matter.
- After updating, call W.grad.zero_() and b.grad.zero_().
What to submit
- Final loss after training and the learned W and b values.
"""

import torch

x = torch.randint(size=(3,2), low=1, high=10, requires_grad=False, dtype=torch.float32)
y = torch.randint(size=(3,), low=1, high=10, requires_grad=False, dtype=torch.float32)

W = torch.randint(size=(2,), low=1, high=10, requires_grad=True, dtype=torch.float32)
b = torch.randint(size=(1,), low=1, high=10, requires_grad=True, dtype=torch.float32)

lr = 0.01




for i in range(50):
	y_hat = x.matmul(W) + b
	mse = torch.nn.MSELoss()
	loss = mse(y_hat, y)
	loss.backward()

	print(i, W, b, loss.item())
	with torch.no_grad():
		W -= lr * (W.grad)
		b -= lr * (b.grad)

	W.grad.zero_()
	b.grad.zero_()

print("final", W, b, y_hat, y, x)
