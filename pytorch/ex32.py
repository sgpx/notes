import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNet(nn.Module):
	def __init__(self):
		super(SimpleNet, self).__init__()
		self.linear = nn.Linear(3, 1)

	def forward(self, x):
		return self.linear(x)


x = torch.randn(5,3)
y_true = torch.randn(5,1)

model = SimpleNet()

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)


y_pred = model(x)
loss = criterion(y_pred, y_true)

print(f"Loss before backward: {loss.item()}")
loss.backward()
optimizer.step()

y_pred = model(x)
loss = criterion(y_pred, y_true)
print(f"Loss after optimizer step: {loss.item()}")
