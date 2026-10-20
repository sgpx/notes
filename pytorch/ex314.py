"""
Problem:

Write a self-contained PyTorch script that trains a small binary classifier with torch.optim.SGD on a synthetic two-class dataset.

Requirements:

Generate a reproducible 2D dataset with two overlapping Gaussian blobs for training and testing.
Build a small neural network classifier (at least one hidden layer) using nn.Module.
Train for a fixed number of epochs using mini-batches from DataLoader, CrossEntropyLoss, and torch.optim.SGD.
Use the optimizer with momentum and a learning rate you choose.
During training, print the average training loss and training accuracy at the end of each epoch.
After training, evaluate on the test set and print the final test accuracy.
Run inference on 5 new sample points and print the predicted class probabilities and predicted labels.
Save the trained model’s state_dict to a file and then load it back into a fresh model instance before doing the final inference pass.

The script should be runnable as-is and should not depend on any external files or datasets.
"""

import torch
import torch.nn as nn
import torch.optim as optim

torch.manual_seed(99)

center1 = torch.rand(2)
print(center1)

center2 = torch.tensor([center1[0], -center1[1]])
print(center2)


noise1 = torch.randn(100,2, dtype=torch.float32)
noise2 = torch.randn(100,2, dtype=torch.float32)

points1 = noise1 + center1
points2 = noise2 + center2

"""

# plotting
import matplotlib.pyplot as plt

plt.scatter(points1[:,0], points1[:,1], color=["red"]*100)
plt.scatter(points2[:,0], points2[:,1], color=["green"]*100)

k = 4*torch.ceil(torch.max(torch.hstack([center1, center2]).flatten()))
print(k)

plt.xlim(-k, k)
plt.ylim(-k, k)
	
plt.show()
"""

X = torch.vstack([points1, points2])
Y = torch.tensor([0]*100 + [1]*100, dtype=torch.long)


class SimpleNN(nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(2, 16)
		self.fc2 = nn.Linear(16, 128)
		self.fc3 = nn.Linear(128, 2) # loss scores for cross entropy loss 
		self.relu = nn.ReLU()

	def forward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.fc2(x)
		x = self.relu(x)
		x = self.fc3(x)
		return x

model = SimpleNN()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
criterion = nn.CrossEntropyLoss()

dataset = torch.utils.data.TensorDataset(X, Y)
train_len, test_len = 160, 40
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_len, test_len])

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=16, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=4, shuffle=False)

NUM_EPOCHS = 10

for epoch in range(NUM_EPOCHS):
	loss_list = []
	acc_list = []
	for x_batch, y_batch in train_loader:
		optimizer.zero_grad()
		y_hat = model(x_batch)
		loss = criterion(y_hat, y_batch)
		loss_list.append(loss.item())
		loss.backward()
		optimizer.step()
		_, preds = torch.max(y_hat, dim=1)
		correct = (preds == y_batch).sum().item()
		num_samples = int(y_batch.size(0))
		training_accuracy = correct / num_samples
		acc_list.append(training_accuracy)
		print("training accuracy", training_accuracy)
	print("epoch avg loss", sum(loss_list) / len(loss_list))
	print("epoch avg training accuracy", sum(acc_list) / len(acc_list))

with torch.no_grad():
	model.eval()
	for x_batch, y_batch in train_loader:
		logits = model(x_batch)
		probs = torch.softmax(logits, dim=1)
		preds = torch.argmax(probs, dim=1)
		correct = (preds == y_batch).sum().item()
		num_samples = int(y_batch.size(0))
		training_accuracy = correct / num_samples
		print("training accuracy", training_accuracy)

	loss_list = []
	acc_list = []
	for x_batch, y_batch in test_loader:	
		logits = model(x_batch)		
		probs = torch.softmax(logits, dim=1)
		preds = torch.argmax(probs, dim=1)
		loss = criterion(logits, y_batch)
		loss_list.append(loss.item())
		correct = (preds == y_batch).sum().item()
		num_samples = int(y_batch.size(0))
		test_accuracy = correct / num_samples
		print("test accuracy", test_accuracy)		
		acc_list.append(test_accuracy)
	print("avg loss", sum(loss_list) / len(loss_list) )	
	print("test accuracy", sum(acc_list) / len(acc_list) )
torch.save(model.state_dict(), "ex314.pt")

model_new = SimpleNN()
model_new.load_state_dict(torch.load("ex314.pt"))

new_pts = center2 + torch.randn(5, 2)

model_new.eval()


with torch.no_grad():
	labels = torch.ones(new_pts.size(0), dtype=torch.long)
	logits = model_new(new_pts)
	probs = torch.softmax(logits, dim=1)
	preds = torch.argmax(probs, dim=1)
	correct = (preds == labels).sum().item()
	num_samples = int(labels.size(0))
	test_accuracy = correct / num_samples
	print("test accuracy:" ,test_accuracy)
	print("Predicted class probabilities:\n", probs)
	print("Predicted labels:\n", preds)
