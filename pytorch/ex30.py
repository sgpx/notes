# Create a simple feedforward neural network with 1 hidden layer to classify the famous Iris dataset. Train your model using cross-entropy loss and an optimizer. This will enhance your understanding of multi-class classification and deep learning.

from sklearn.datasets import load_iris

iris_data = load_iris(as_frame=True)
y = iris_data.target
X = iris_data.data

import torch
import torch.nn as nn

class SimpleNN(nn.Module):
	def __init__(self, input_size, hidden_size, output_size):
		super(SimpleNN, self).__init__()
		self.hidden = nn.Linear(input_size, hidden_size)
		self.output = nn.Linear(hidden_size, output_size)

	def forward(self, x):
		x = torch.relu(self.hidden(x))
		x = self.output(x)
		return x	


# input_size = number of input features
# hidden_size = number of neurons in hidden layer
# output_size = number of output classes


input_size= X.shape[1]
hidden_size = 8
output_size = len(set(y))

model = SimpleNN(input_size, hidden_size, output_size)

# Define loss function and optimizer
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Prepare data for training
X_train = torch.tensor(X.values, dtype=torch.float32)
y_train = torch.tensor(y.values, dtype=torch.long)

# Train the model
for epoch in range(100):
	optimizer.zero_grad()  # Clear gradients w.r.t. parameters
	output = model(X_train)  # Forward pass: Compute predicted y by passing x to the model
	loss = loss_fn(output, y_train)  # Compute loss
	loss.backward()  # Backward pass: Compute gradient of the loss with respect to model parameters
	optimizer.step()  # Perform a single optimization step (parameter update)
	print('Epoch {}: train loss: {}'.format(epoch, loss.item()))

# Test the model
with torch.no_grad():
	y_pred = model(X_train)
	_, predicted = torch.max(y_pred, 1)
	accuracy = (predicted == y_train).sum().item() / y_train.size(0)
	print('Accuracy: {}'.format(accuracy))
