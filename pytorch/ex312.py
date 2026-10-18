"""
Write a custom nn.Module containing a single nn.Linear layer. In its forward method, accept a batch of 2D images (shape [8, 1, 28, 28]), apply a 90-degree counterclockwise rotation to the spatial dimensions using torch.rot90, flatten the spatial and channel dimensions using torch.flatten, and pass the result through the linear layer to output 10 class logits. Run one forward pass with dummy data to verify the output shape is [8, 10].
"""

import torch
import torch.nn as nn

class SimpleNN(nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(28**2, 10)

	def forward(self, x):
		x = torch.rot90(x, dims=(2,3))
		x = torch.flatten(x, start_dim=1)
		x = self.fc1(x)
		return x

x = torch.rand(8, 1, 28, 28)
model = SimpleNN()
y = model(x)
print(y, y.shape)
