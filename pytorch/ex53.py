import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

NUM_EPOCHS = 500

N = 10000
x = torch.rand(N, 1)
#noise = 0.1*torch.randn(N, 1)
noise = (torch.rand(N, 1) - 0.5) * 0.2
y_true = torch.sin(2*(np.pi)*x) + noise

## model = nn.Linear(1, 1)

class SimpleNet(nn.Module):
	def __init__(self):
		super(SimpleNet, self).__init__()
		self.relu = nn.ReLU(inplace=True)
		self.l1 = nn.Linear(1,30)
		self.l2 = nn.Linear(30,15)
		self.l3 = nn.Linear(15,4)
		self.l4 = nn.Linear(4,1)

	def forward(self, x):
		x = self.l1(x)
		x = self.relu(x)
		x = self.l2(x)
		x = self.relu(x)
		x = self.l3(x)
		x = self.relu(x)
		x = self.l4(x)
		return x

model = SimpleNet()
y_pred = model(x)
criterion = nn.MSELoss()

#optimizer = optim.SGD(model.parameters(), lr=0.01)

optimizer = optim.Adam(model.parameters(), lr=0.01)

for e in range(NUM_EPOCHS):
	print(e)
	optimizer.zero_grad()
	y_pred = model(x)
	loss = criterion(y_pred, y_true)
	loss.backward()
	optimizer.step()
	print(e, loss.item())

#x_test = torch.tensor([[5]], dtype=torch.float32)
x_test = torch.rand(N, 1)
y_true = torch.sin(2*(np.pi)*x_test)
y_pred = model(x_test)
diff = y_true - y_pred

print(y_true, y_pred, diff)

sorted_indices = torch.argsort(x_test, dim=0).flatten()

# Reorder x, true y, and predicted y using those indices
x_test_sorted = x_test[sorted_indices]
y_true_sorted = y_true[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]

import matplotlib.pyplot as plt
# Plot the sorted values
plt.plot(x_test_sorted.detach().numpy(), y_true_sorted.detach().numpy(), label="True")
plt.plot(x_test_sorted.detach().numpy(), y_pred_sorted.detach().numpy(), label="Predicted")
plt.legend()
plt.show()
