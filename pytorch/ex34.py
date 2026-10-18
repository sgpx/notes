"""

Define a neural network model (SmallNet) as a subclass of nn.Module with the following architecture:

    Linear layer transforming input features of size 20 to 64 nodes
    ReLU activation
    Linear layer from 64 to 32 nodes
    ReLU activation
    Linear layer from 32 to 2 output nodes (for 2 classes)


""" 

import torch
import torch.nn as nn
import torch.optim as optim


class SmallNet(nn.Module):
	def __init__(self):
		super(SmallNet, self).__init__()
		self.relu = nn.ReLU()
		self.l1 = nn.Linear(20, 64)
		self.l2 = nn.Linear(64, 32)
		self.l3 = nn.Linear(32, 2)

	def forward(self, x):
		x = self.l1(x)
		x = self.relu(x)
		x = self.l2(x)
		x = self.relu(x)		
		x = self.l3(x)		
		return x		
