"""
Generate synthetic regression data (y = 3x + 2 + noise) with 4096 samples. Define a small 2-layer ReLU network. Use a DataLoader with batch size 256, but accumulate gradients over 4 mini-batches (effective batch size = 1024) before each optimizer step. Train for 20 epochs, print the loss every epoch, and verify the learned slope is close to 3. Keep the script under 40 lines.
"""

import torch
import torch.nn as nn
import torch.optim as optim

N = 4096
BATCH_SIZE = 256
EFFECTIVE_BATCH_SIZE = 1024
NUM_EPOCHS = 20

DIVISOR = EFFECTIVE_BATCH_SIZE // BATCH_SIZE

class SimpleNN(nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(1, 10)
		self.fc2 = nn.Linear(10, 1)
		self.relu = nn.ReLU()

	def forward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.fc2(x)
		return x

X = torch.rand(N, 1)
noise = torch.randn(N, 1)
model = SimpleNN()

Y = (3*X) + 2 + noise

dataset = torch.utils.data.TensorDataset(X, Y)
test_frac = 0.0 # for future use
test_size = int(test_frac * N) 
train_size = N - test_size
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])
train_loader = torch.utils.data.DataLoader(train_dataset, shuffle=True, batch_size=BATCH_SIZE)
test_loader = torch.utils.data.DataLoader(test_dataset, shuffle=False, batch_size=BATCH_SIZE)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(NUM_EPOCHS):
	optimizer.zero_grad()
	ctr = 0
	epoch_loss = 0
	for x_batch, y_batch in train_loader:
		ctr += 1

		y_hat = model(x_batch)
		loss = criterion(y_hat, y_batch)
		epoch_loss += loss.item()
		loss /= DIVISOR
		loss.backward()

		if ctr == DIVISOR:
			optimizer.step()	
			optimizer.zero_grad()
			ctr = 0

	if ctr:
		optimizer.step()	
	print(epoch, epoch_loss)


with torch.no_grad():
    slope = (model.fc2.weight @ model.fc1.weight).item()
    print("learned slope:", slope)
