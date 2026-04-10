# Problem:
# Learn to predict the square of a number. Given an input number (x), the model should output (x^2).

import torch
import torch.nn as nn
import torch.optim as optim

NUM_SAMPLES = 100
NUM_TRAIN = int(NUM_SAMPLES * (3/4))
NUM_EPOCHS = 100

class SimpleNN(nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(1,4)
		self.relu = nn.ReLU()
		self.fc2 = nn.Linear(4,1)

	def forward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.fc2(x)

model = SimpleNN()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

x_true = torch.randint(1,100,size=(1,NUM_SAMPLES),dtype=torch.float32)
y_true = x_true ** 2
y_true += torch.randn(1,NUM_SAMPLES)

indices = torch.randperm(NUM_SAMPLES)
train_idx = indices[:NUM_TRAIN]
test_idx = indices[NUM_TRAIN:]

x_train = x_true[0, train_idx]
x = x_train.unsqueeze(1)
print(x)
y_train = y_true[0, train_idx]
x_test = x_true[0, test_idx]
y_test = y_true[0, test_idx]


for epoch in range(NUM_EPOCHS):
	optimizer.zero_grad()
	y_hat = model(x_train)
	loss = criterion(y_true, y_hat.unsqueeze(1))
	loss.backward()
	optimizer.step()
	print(epoch, loss.item())

