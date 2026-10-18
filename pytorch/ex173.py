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

Problem 5 — Mini-batch training with DataLoader
Goal: Learn how to use a DataLoader to feed data in batches.
What to do
- Create a small dataset (8 samples) for a simple linear problem:
  X and y as in Problem 4 but with more samples, e.g. a simple linear relation y = 1.5*x0 + -2.0*x1 + 0.5
- Use torch.utils.data.TensorDataset and torch.utils.data.DataLoader with batch_size=2.
- Use the same manual update rule as Problem 4, but update parameters after each batch.
- Train for a few epochs (e.g., 3) and print the loss every epoch.
Hints
- Build dataset like: dataset = TensorDataset(X, y); loader = DataLoader(dataset, batch_size=2, shuffle=True)
- In the batch loop, compute loss on the batch, backward, and update.
What to submit
- The loss printed after each epoch and a couple of example predicted vs. true values.
"""

import torch

rx = torch.randint(size=(3,2), low=1, high=10, requires_grad=False, dtype=torch.float32)
ry = torch.randint(size=(3,), low=1, high=10, requires_grad=False, dtype=torch.float32)

class TinyDataset(torch.utils.data.Dataset):
	def __init__(self):
		self.X = rx
		self.y = ry

	def __len__(self):
		return len(self.y)

	def __getitem__(self, idx):
		return self.X[idx], self.y[idx]


dataset = TinyDataset()
dataloader = torch.utils.data.DataLoader(dataset, batch_size=3, shuffle=True)

W = torch.randint(size=(2,), low=1, high=10, requires_grad=True, dtype=torch.float32)
b = torch.randint(size=(1,), low=1, high=10, requires_grad=True, dtype=torch.float32)

lr = 0.01

for i in range(50):
	for x_batch, y_batch in dataloader:
	
		y_hat = x_batch.matmul(W) + b
		loss = torch.nn.MSELoss()(y_hat.squeeze(), y_batch)
		loss.backward()

		with torch.no_grad():

			W -= lr * (W.grad)
			b -= lr * (b.grad)

		W.grad.zero_()
		b.grad.zero_()

		print(x_batch, y_batch, W, b)
