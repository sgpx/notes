import torch

x_base = torch.rand(20, 1)
y_base = 2*x_base + 1
#bias = torch.randn(20, 1)

#y_base += bias

W = torch.zeros(size=(20, 1), requires_grad=True)
b = torch.zeros(size=(20, 1), requires_grad=True)

class FNN(torch.nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = torch.nn.Linear(1, 32)
		self.fc2 = torch.nn.Linear(32, 8)
		self.fc3 = torch.nn.Linear(8, 1)
		self.relu = torch.nn.ReLU()

	def forward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.fc2(x)
		x = self.relu(x)
		x = self.fc3(x)
		return x

model = FNN()
optimizer = torch.optim.Adam([W,b])

NUM_EPOCHS = 1000
	
mse = torch.nn.MSELoss()

for epoch in range(NUM_EPOCHS):
	y_hat = model(W*x_base + b)
	optimizer.zero_grad()
	loss = mse(y_hat, y_base)
	loss.backward()
	optimizer.step()	
	print("epoch", epoch, "loss", loss.item())

print("y_hat: ", y_hat)
print("y_base: ", y_base)
print("W: ", W)
print("b: ", b)
