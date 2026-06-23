# Use torch.nn.functional.one_hot to convert class indices to one‑hot vectors and shows how to feed them into a model.

import torch
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset


num_classes = 4

x_true = torch.randint(size=(100,4), low=1, high=10)
y_true = x_true.pow(2) % num_classes
print(y_true.shape)

for i in y_true:
	print(i)
	one_hot_vectors = F.one_hot(i, num_classes=num_classes)
	print(one_hot_vectors.shape)

class FNN(nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(4,2)
		self.fc2 = nn.Linear(2,1)
		self.relu = nn.ReLU()

	def backward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.fc2(x)
		return x


model = FNN()
optimizer = optim.SGD(model.parameters(), lr=0.01)


