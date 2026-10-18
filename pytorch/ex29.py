import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

class LinearRegressionModel(nn.Module):
	def __init__(self):
		super(LinearRegressionModel, self).__init__()
		self.linear = nn.Linear(1,1)

	def forward(self, x):
		return self.linear(x)



torch.manual_seed(0)

x = np.random.rand(100,1) * 10
true_slope = 2.0
true_intercept = 5.0

y = true_slope * x + true_intercept + np.random.randn(100,1) # add some noise

X = torch.FloatTensor(x)
Y = torch.FloatTensor(y)

model = LinearRegressionModel()

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

num_epochs = 1000
for epoch in range(num_epochs):
	model.train()

	outputs = model(X)
	loss = criterion(outputs, Y)

	optimizer.zero_grad()
	loss.backward()
	optimizer.step()

	print(epoch + 1, "loss", loss.item())


model.eval()
with torch.no_grad():
	predicted = model(X).detach().numpy()

plt.scatter(x, y, label='Original data')
plt.plot(x, predicted, label='Fitted line', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression with PyTorch')
plt.legend()
plt.show()

def mse(y_true, y_pred):
	return np.mean((y_true - y_pred)**2)


def rmse(y_true, y_pred):
	return np.sqrt(mse(y_true, y_pred))

print("MSE", mse(predicted, y))
print("RMSE", rmse(predicted, y))
