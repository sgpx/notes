# Implements a manual linear regression loop (y = wx + b) using autograd, with a simple SGD optimizer and prints loss each epoch.

import torch

NUM_EPOCHS = 100
N = 100
x = torch.linspace(-5,5,N)
orig_W = 2
orig_B = -5
y = orig_W*x + orig_B
w = torch.tensor([0], requires_grad=True, dtype=torch.float32)
b = torch.tensor([0], requires_grad=True, dtype=torch.float32)

optimizer = torch.optim.SGD((w,b), lr=0.1)

for epoch in range(NUM_EPOCHS):
	optimizer.zero_grad()
	y_hat = w*x + b
	loss = (y - y_hat).pow(2).mean()
	loss = torch.sqrt(loss)
	loss.backward()		
	optimizer.step()
	print(loss)

print(orig_W, w, "\n", orig_B, b)
