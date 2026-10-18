import torch

x = torch.randn(1000, 1)
x = 2.5 * x

print(x)
y = torch.relu(x)
#y = torch.where(True, torch.max(x, 0), 0) 

dataset = torch.utils.data.TensorDataset(x, y)
loader = torch.utils.data.DataLoader(dataset, batch_size=10, shuffle=True)

model = torch.nn.Sequential(
	torch.nn.Linear(1,16),
	torch.nn.ReLU(),
	torch.nn.Linear(16,1),
)

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
mse = torch.nn.MSELoss()

for epoch in range(100):
	total = 0
	for x_batch, y_batch in loader:
		optimizer.zero_grad()
		y_hat = model(x_batch)
		loss = mse(y_batch, y_hat)
		loss.backward()
		optimizer.step()	
		total += loss.item()
	print("epoch", epoch, "total loss", total)
