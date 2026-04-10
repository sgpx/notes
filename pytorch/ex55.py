# Goal: Use PyTorch to create a simple linear regression model that learns the relationship between input x and output y, where y = 3x^5 + 4x^4 + noise. We will generate the data with torch.randn().

import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNet(nn.Module):
	def __init__(self):
		super(SimpleNet, self).__init__()
		self.l1 = nn.Linear(1,5)
		self.l2 = nn.Linear(5,10)
		self.l3 = nn.Linear(10,5)
		self.l4 = nn.Linear(5,1)
		self.relu = nn.ReLU(inplace=True)

	def forward(self, x):
		x = self.l1(x)
		x = self.relu(x)
		x = self.l2(x)
		x = self.relu(x)
		x = self.l3(x)
		x = self.relu(x)
		x = self.l4(x)
		return x

x = torch.randn(100, 1)
print(x)
noise = 0.1 *  torch.randn(100, 1)
y_true = 3*(x**5) + 4*(x**4) + noise

print(x.shape)
print(y_true.shape)
model = SimpleNet()

y_pred = model(x)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

NUM_EPOCHS = 1000

for epoch in range(NUM_EPOCHS):
	optimizer.zero_grad()
	y_pred = model(x)
	loss = criterion(y_pred, y_true)
	loss.backward()
	optimizer.step()
	print(epoch, loss.item())

idx = torch.argsort(x.squeeze())

x = x[idx]
y_true = y_true[idx]
y_pred = y_pred[idx]

import matplotlib.pyplot as plt

plt.plot(x.detach().numpy(), y_true.detach().numpy(), label="True")
plt.plot(x.detach().numpy(), y_pred.detach().numpy(), label="Predicted")
plt.legend()
plt.show()
