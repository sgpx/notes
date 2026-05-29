"""
Problem
- Task: Learn to approximate the function y = max(0, x) (a basic ReLU) from data.
- Why it’s easy: It’s a simple, non-linear function that a small neural network with a ReLU hidden layer should learn quickly.

Data
- Input x sampled from [-5, 5].
- Target y = max(0, x).

Model
- A tiny feedforward network with one hidden layer and ReLU activation:
  - Input -> Linear(1 -> 16) -> ReLU -> Linear(16 -> 1)

Training
- Loss: Mean Squared Error (MSE)
- Optimizer: Adam
- Epochs: a few hundred
- Evaluation: check that predictions resemble max(0, x)
"""

import torch
import torch.nn as nn
import torch.optim as optim

x = torch.randint(size=(100,1), low=-5, high=6, dtype=torch.float32)
print(x)

y = torch.clamp(x, min=0.0)
print(y)

model = nn.Sequential(
	nn.Linear(1,16),
	nn.ReLU(),
	nn.Linear(16,1),
)


mse = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for i in range(100):
	y_hat = model(x)
	loss = mse(y_hat, y)
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()
	print("loss", i, loss.item())

with torch.no_grad():
	x_test = torch.linspace(-5,5,21).unsqueeze(1)
	print(x_test)
	y_pred = model(x_test)
	print(torch.cat([x_test, y_pred], dim=1))
