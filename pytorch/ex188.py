import torch
import sys

device_name = "mps"
device_name = "cpu"
device_name = sys.argv[-1]

TENSOR_DIM = 10**8

x_base = torch.rand(TENSOR_DIM, 1)
y_base = 2*x_base + 1

x_base = x_base.to(device_name)
y_base = y_base.to(device_name)

W = torch.tensor(0, requires_grad=True, dtype=torch.float32, device=device_name)
b = torch.tensor(0, requires_grad=True, dtype=torch.float32, device=device_name)

W = W.to(device_name)
b = b.to(device_name)

optimizer = torch.optim.SGD([W,b], lr=0.01)

NUM_EPOCHS = 5000
	
mse = torch.nn.MSELoss()

for epoch in range(NUM_EPOCHS):
	y_hat = W*x_base + b
	loss = mse(y_hat, y_base)
	loss.backward()
	optimizer.step()	
	optimizer.zero_grad()
	#print("epoch", epoch, "loss", loss.item())

print("y_hat: ", y_hat)
print("y_base: ", y_base)
print("W: ", W)
print("b: ", b)
print("device: ", device_name)
