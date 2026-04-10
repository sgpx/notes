import torch
import torch.nn as nn
import torch.optim as optim

VOCAB = 5000

class SNN(nn.Module):
	def __init__(self):
		super().__init()
		self.fc1 = nn.Linear(VOCAB, 2500)
		self.fc2 = nn.Linear(2500, 1250)
		self.fc3 = nn.Linear(1250, 625)
		self.fc4 = nn.Linear(625,312)
		self.fc5 = nn.Linear(312, 156)
		self.fc6 = nn.Linear(156, 78)
		self.fc7 = nn.Linear(78, 39)
		self.fc8 = nn.Linear(39, 19)
		self.fc9 = nn.Linear(19, 9)
		self.fc10 = nn.Linear(9, 5)

	def forward(self, x):
		x = self.relu(self.fc1(x))
		x = self.relu(self.fc2(x))
		x = self.relu(self.fc3(x))
		x = self.relu(self.fc4(x))
		x = self.relu(self.fc5(x))
		x = self.relu(self.fc6(x))
		x = self.relu(self.fc7(x))
		x = self.relu(self.fc8(x))
		x = self.relu(self.fc9(x))
		x = self.fc10(x)  # logits for final output
		return x		

a = SNN()


