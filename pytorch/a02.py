import torch
import torch.nn as nn
import torch.optim as optim

class SFFN(nn.Module):
	def __init__(self, input_size, hidden_layer_size, output_layer_size):
		super(SFFN, self).__init__()
		self.hidden = nn.Linear(input_size, hidden_layer_size)
		self.relu = nn.ReLU()
		self.output = nn.Linear(hidden_layer_size, output_layer_size)

	def forward(self, x):
		x = self.hidden(x)
		x = self.relu(x)
		x = self.output(x)
		return x



input_size = 2
hidden_size = 3
output_size = 1
learning_rate = 0.01
epochs = 1000

X_train = torch.tensor([[1,2],[3,4]], dtype=torch.float32)
y_train = torch.tensor([[1]], dtype=torch.float32)

model = SFFN(2, 3, 1)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

for epoch in range(epochs):
	y_pred = model(X_train)
	loss = criterion(y_pred, y_train)
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()
	if (epoch + 1) % 100 == 0:
		print("epoch", epoch+1)
		print("loss", loss.item())

with torch.no_grad():
	predictions = model(X_train)
	print("predictions", predictions)
