# Write a PyTorch program to manually compute the gradient of the Cross-Entropy Loss for a 3-class prediction without using torch.nn.functional.cross_entropy.
import torch
import torch.nn as nn
import torch.optim as optim


N = 100

X = torch.rand(N, 5)
y_true = nn.functional.one_hot(torch.randint(low=0, high=3, size=(N,)))

print(X, y_true)

class SimpleNN(nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(5, 8)
		self.fc2 = nn.Linear(8, 3)
		self.relu = nn.ReLU()

	def forward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.fc2(x)
		return x


model = SimpleNN()
y_pred = model(X)
y_pred.retain_grad()
p = torch.softmax(y_pred, dim=1)
p = torch.clamp(p, min=1e-10, max=1.0)
print(p)

prod = y_true * torch.log(p)

grad_logits = (p - y_true)/N

loss = -torch.sum(y_true * torch.log(p), dim=1).mean()
loss.backward()

print(torch.allclose(y_pred.grad, grad_logits))
