"""
**Build a complete multi-class classification pipeline using `nn.Module` with training, validation, and test evaluation.**

Practical challenge:  
Implement a PyTorch neural network for MNIST digit classification with the following:  
- A custom `nn.Module` model with at least two hidden layers.  
- Use `torchvision.datasets.MNIST` and `DataLoader` for train/val/test splits.  
- Train with cross-entropy loss and an optimizer (e.g., Adam).  
- After each epoch, evaluate and print both train and validation accuracy.  
- After training, compute test accuracy and save the model.  
- Bonus: Implement early stopping if validation loss doesn’t improve for N epochs.  

This will solidify your understanding of data pipelines, model structure, training loops, evaluation, and basics of overfitting/early stopping.
"""
import torch
import torch.nn as nn
import torch.optim as optim


NUM_EPOCHS = 100
N = 10

device = torch.device("mps")

class FNN(nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(28**2, 128)
		self.fc2 = nn.Linear(128, 64)
		self.fc3 = nn.Linear(64, 32)
		self.fc4 = nn.Linear(32, 10)
		self.dropout = nn.Dropout(p=0.05)
		self.relu = nn.ReLU()

	def forward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.dropout(x)
		x = self.fc2(x)
		x = self.relu(x)
		x = self.dropout(x)
		x = self.fc3(x)
		x = self.relu(x)
		x = self.fc4(x)
		return x

from torchvision import datasets
from torchvision import transforms

transform = transforms.Compose([
	transforms.ToTensor(),
	transforms.Normalize((0.1307,), (0.3081,)) 
])

train_dataset = datasets.MNIST("./mnist", train=True, download=True, transform=transform)
test_dataset = datasets.MNIST("./mnist", train=False, download=True, transform=transform)

from torch.utils.data import DataLoader, random_split

train_size = int(len(train_dataset) * 0.9)
val_size = len(train_dataset) - train_size
train_dataset, val_dataset = random_split(train_dataset, [train_size, val_size])

batch_size = 64

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)


model = FNN().to(device)
cse = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

def evaluate_model(model, data_loader):
	model.eval()
	running_loss = 0
	correct = 0
	total = 0
	with torch.no_grad():
		for x_batch, y_batch in data_loader:
			x_batch, y_batch = x_batch.to(device), y_batch.to(device)
			x_batch = x_batch.view(x_batch.size(0), -1)
			outputs = model(x_batch)
			loss = cse(outputs, y_batch)
			running_loss += (loss.item() * y_batch.size(0))
			_, predicted = torch.max(outputs, 1)
			correct += (predicted == y_batch).sum().item()
			total += y_batch.size(0)
	accuracy = correct / total
	overall_loss = running_loss / total
	return accuracy, overall_loss

best_loss = float('inf')
patience_counter = 0
best_model_state = None

for epoch in range(NUM_EPOCHS):
	model.train()
	for x_batch, y_batch in train_loader:
		x_batch, y_batch = x_batch.to(device), y_batch.to(device)
		x_batch = x_batch.view(x_batch.size(0), -1)
		y_hat = model(x_batch)
		loss = cse(y_hat, y_batch)
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()
	acc, overall_loss = evaluate_model(model, val_loader)
	if overall_loss < best_loss:
		patience_counter = 0
		best_loss = overall_loss
		best_model_state = {k: v.clone() for k,v in model.state_dict().items()}
	else:
		patience_counter += 1
	if patience_counter == N:
		print("not improving, stopping the loop")
		break
	train_acc, tl = evaluate_model(model, train_loader)
	print(f"Epoch {epoch+1}: Train Accuracy: {train_acc:.4f}, Validation Accuracy: {acc:.4f}, Patience: {patience_counter}/{N}")


if best_model_state is not None:
	torch.save(best_model_state, "mnist_fnn.pth")
	model.load_state_dict(best_model_state)

test_acc, test_loss = evaluate_model(model, test_loader)
print(f"Test Accuracy: {test_acc:.4f}, Test Loss: {test_loss:.4f}")
