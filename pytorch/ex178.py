import torch

x = torch.randn(100)
x = x.unsqueeze(1)
print(x)
y = 2*x + 1

print(y)
model = torch.nn.Linear(1,1)

mse = torch.nn.MSELoss()

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for i in range(100):
	y_hat = model(x)
	loss = mse(y_hat, y)
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()
	print(loss.item())
