import torch
import torch.nn as nn

class MyModel(nn.Module):
	def __init__(self):
		super().__init__()
		self.linear = nn.Linear(1, 5)
		self.relu = nn.ReLU()
		self.linear2 = nn.Linear(5, 1)
	def forward(self, x):
		x = self.linear(x)
		x = self.relu(x)
		x = self.linear2(x)
		return x

model = MyModel()
x = torch.tensor([5.1], requires_grad=True)
y = model(x)

print(x, y)
