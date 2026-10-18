"""
Train a tiny classifier on synthetic data.
Data: 300 points in 2D, 3 clusters.
Model: nn.Sequential(Linear(2,16), ReLU, Linear(16,3)).
Training: cross_entropy, Adam with lr 0.05, 100 full-batch steps, printing the loss every 20 steps.
Evaluation: report final accuracy using your #2 code inside no_grad (expect above 90%).
"""

import torch
import torch.nn as nn
import torch.optim as optim

centers = torch.randint(size=(3,2), low=-10, high=10)
print(centers)

x = torch.stack([(center + torch.rand(100,2)) for center in centers]).reshape(300,2).to(torch.float32)
y = torch.stack([ torch.zeros(100), torch.ones(100), torch.ones(100)*2 ]).reshape(300).to(torch.long)
print(x.shape)
print(y, y.shape)

model = nn.Sequential(nn.Linear(2,16), nn.ReLU(), nn.Linear(16,3))
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.05)

for b in range(100):
	optimizer.zero_grad()
	y_hat = model(x)
	loss = criterion(y_hat, y)
	loss.backward()
	optimizer.step()
	if b % 20 == 0: print(loss.item())

with torch.no_grad():
	logits = model(x)
	targets = y
	preds = torch.argmax(logits, dim=1)
	res = preds == targets
	print(res.float().mean())
