# Defines a tiny feed‑forward network (2‑layer linear + ReLU) and trains it for 5 epochs on a 2‑D synthetic dataset.

import torch

NUM_EPOCHS = 5

synthetic_data = torch.randn(5,5) # shape = (5,5)
X_train = synthetic_data[:,:4] # shape = (4,5) 
y_train = synthetic_data[:,4] # shape = (1,5)
y_train = y_train.squeeze() # shape = (5,)

class FNN(torch.nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = torch.nn.Linear(4,2)
		self.fc2 = torch.nn.Linear(2,1)
		self.relu = torch.nn.ReLU()

	def forward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.fc2(x)
		return x


model = FNN()
mse = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

y_hat = model(X_train)
loss = mse(y_hat, y_train.unsqueeze(1))

print("loss")
print(y_hat.shape)
print(y_train.shape)
print(y_train.unsqueeze(1).shape)

loss.backward()

for epoch in range(NUM_EPOCHS):
	optimizer.zero_grad()
	y_hat = model(X_train)
	loss = mse(y_hat, y_train.unsqueeze(1))
	loss.backward()	
	optimizer.step()		
