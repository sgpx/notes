"""
## Problem 1: 2-Layer Neural Network for Regression

Write code that creates a 2-layer network (input→linear→relu→linear) that maps a 5-dimensional input to a 1-dimensional output and trains it on 100 random points.

- Use `torch.nn.Linear` and `torch.nn.functional.relu`
- Train the network for 10 epochs with SGD optimizer and print the loss after each epoch
- After training, test the model on a new input tensor `[[1,0,0,0,0]]` and print the result
"""

import torch
import torch.nn as nn
import torch.optim as optim

NUM_EPOCHS = 10

class SimpleNN(nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(5,3)
		self.fc2 = nn.Linear(3,1)

	def forward(self, x):
		x = self.fc1(x)
		x = nn.functional.relu(x)
		x = self.fc2(x)
		return x

x_true = torch.randint(low=0, high=10, size=(100,5)).to(dtype=torch.float32)
y_true = torch.randint(low=0, high=10, size=(100,1)).to(dtype=torch.float32)

model = SimpleNN()
optimizer = optim.SGD(model.parameters(), lr=0.01)

criterion = nn.MSELoss()


NUM_EPOCHS

for _ in range(NUM_EPOCHS):
	optimizer.zero_grad()
	y_hat = model(x_true)
	loss = criterion(y_hat, y_true)
	loss.backward()
	optimizer.step()

with torch.no_grad():
	model.eval()
	x_test = torch.tensor([[1,0,0,0,0]], dtype=torch.float32)
	y_pred = model(x_test)
	print(y_pred)
