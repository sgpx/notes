"""

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
from torch.utils.data import TensorDataset, DataLoader

X = torch.randn(8, 2)
print(X)

x0 = X[:,0]
print(x0)

x1 = X[:, 1]
print(x1)

y = (1.5 * x0) - (2.0 * x1) + 0.5
print(y)

y = y.unsqueeze(1)
print(y)

print(y)

dataset = TensorDataset(X, y)


loader = DataLoader(dataset, batch_size=2)
loss = torch.nn.MSELoss()
model = torch.nn.Linear(2, 1)

lr = 0.01
total_loss = 0
loss_fn = torch.nn.MSELoss()

for epoch in range(3):
	for x_batch, y_batch in loader:
		print(">>>", x_batch, y_batch)
		preds = model(x_batch)
		loss = loss_fn(preds, y_batch)
		loss.backward()

		with torch.no_grad():
			for param in model.parameters():
				param.data -= lr * param.grad

		model.zero_grad()

		li = loss.item()
		print("loss: ", li)
		total_loss += li

	print("epoch", epoch, "total loss", total_loss)

	
print(total_loss)
