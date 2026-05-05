import torch

x_base = torch.rand(20, 1)
y_base = 2*x_base + 1

W = torch.tensor(0, requires_grad=True, dtype=torch.float32)
b = torch.tensor(0, requires_grad=True, dtype=torch.float32)


optimizer = torch.optim.Adam([W,b], lr=0.01)

NUM_EPOCHS = 1000
	
mse = torch.nn.MSELoss()

for epoch in range(NUM_EPOCHS):
	y_hat = W*x_base + b
	optimizer.zero_grad()
	loss = mse(y_hat, y_base)
	loss.backward()
	optimizer.step()	
	print("epoch", epoch, "loss", loss.item())

print("y_hat: ", y_hat)
print("y_base: ", y_base)
print("W: ", W)
print("b: ", b)
