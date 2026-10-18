import torch
import torch.nn as nn
import torch.optim as optim

x = 0.1 * torch.randn(100, 1)
noise = 0.1 * torch.rand(100, 1)
y = (2*x) + 3 + noise

model = nn.Linear(1,1)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(100):
	optimizer.zero_grad()
	outputs = model(x)
	loss = criterion(outputs, y)
	loss.backward()
	optimizer.step()
	if (epoch+1) % 20 == 0:
		print(f"epoch : {epoch} # loss : {loss.item()}")

test_input = torch.tensor(([[0.5]]))
predicted = model(test_input).item()

actual = 2*test_input + 3

print(f"input : {test_input}, pred: {predicted}, actual: {actual}")

"""
To use zero-mean Gaussian noise instead of uniform noise for your data, you should generate noise from a normal distribution with mean 0 and some standard deviation (e.g., 0.1). In PyTorch, you can use `torch.randn()` to generate samples from a standard normal distribution (mean 0, std 1), then scale it by your desired std deviation.



### Key changes:
- `noise = 0.1 * torch.randn(100, 1)` generates Gaussian noise with mean 0 and std 0.1.
- Changed `test_input` to 2D tensor `torch.tensor([[0.5]])` so it matches the model input shape `(batch_size, features)`.
"""
