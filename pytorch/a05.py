import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from torch.utils.data import DataLoader
from torchvision import transforms

device_id = "mps" if torch.mps.is_available() else "cpu"

class CIFARNet(nn.Module):
	def __init__(self):
		super().__init__()

		self.layer1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
		self.layer2 = nn.BatchNorm2d(32)
		self.relu = nn.ReLU()
		self.layer3 = nn.MaxPool2d(2,stride=2)
		self.dropout1 = nn.Dropout(0.5)
		self.layer4 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
		self.layer5 = nn.BatchNorm2d(64)
		self.layer6 = nn.MaxPool2d(2,stride=2)
		self.dropout2 = nn.Dropout(0.5)
		self.layer7 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
		self.layer8 = nn.BatchNorm2d(128)
		self.layer9 = nn.MaxPool2d(2,stride=2)
		self.dropout3 = nn.Dropout(0.5)
		self.fc1 = nn.Linear(2048,128)
		self.fc2 = nn.Linear(128,64)
		self.fc3 = nn.Linear(64,32)
		self.fc4 = nn.Linear(32,10)

	def forward(self, x):
		x = self.layer1(x)
		x = self.layer2(x)
		x = self.relu(x)
		x = self.layer3(x)
		x = self.dropout1(x)
		x = self.layer4(x)
		x = self.layer5(x)
		x = self.relu(x)
		x = self.layer6(x)
		x = self.dropout2(x)
		x = self.layer7(x)
		x = self.layer8(x)
		x = self.relu(x)
		x = self.layer9(x)
		x = self.dropout3(x)
		x = self.fc1(torch.flatten(x, 1))
		x = self.relu(x)

		x = self.fc2(x)
		x = self.relu(x)

		x = self.fc3(x)
		x = self.relu(x)

		x = self.fc4(x)
		return x

cifar_mean = [0.4914, 0.4822, 0.4465]
cifar_std = [0.2023, 0.1994, 0.2010]

train_transforms = torchvision.transforms.Compose([
	transforms.RandomHorizontalFlip(),
	transforms.RandomCrop(32,padding=4),
	transforms.ToTensor(),
	transforms.Normalize(mean=cifar_mean, std=cifar_std)
])

test_transforms = torchvision.transforms.Compose([
	transforms.ToTensor(),
	transforms.Normalize(mean=cifar_mean, std=cifar_std)
])


train_dataset = torchvision.datasets.CIFAR10(download=True, root=".", transform=train_transforms)
test_dataset = torchvision.datasets.CIFAR10(download=True, root=".", transform=test_transforms)

train_dataloader = DataLoader(train_dataset, batch_size=128, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=128, shuffle=False) # false because we do not want to shuffle testing data

model = CIFARNet()
model.to(device_id)
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
criterion = nn.CrossEntropyLoss()
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.1)


NUM_EPOCHS = 3

def evaluate(model, test_dataloader, device=device_id):
	model.eval()
	correct = 0
	total = 0
	with torch.no_grad():
		for inputs, labels in test_dataloader:
			inputs, labels = inputs.to(device), labels.to(device)
			outputs = model(inputs)
			_, predicted = torch.max(outputs.data, 1)
			total += labels.size(0)
			correct += (predicted == labels).sum().item()
	accuracy = 100 * correct / total
	model.train()
	return accuracy

best_accuracy = float("-inf")
for epoch in range(NUM_EPOCHS):
	total_loss = 0
	for batch_idx, batch in enumerate(train_dataloader):
		data, targets = batch
		data, targets = data.to(device_id), targets.to(device_id)
		optimizer.zero_grad()
		outputs = model(data)
		loss = criterion(outputs, targets)
		batch_loss = loss.item()
		total_loss += batch_loss
		print(f"batch : {batch_idx} || loss : {batch_loss}")
		loss.backward()
		optimizer.step()

	print("total_loss", total_loss/len(train_dataloader))
	test_accuracy = evaluate(model, test_dataloader)

	print(f"epoch : {epoch+1}, acc : {test_accuracy}")
	if test_accuracy > best_accuracy:
		best_accuracy = test_accuracy
		torch.save({"epoch": epoch+1, "model_state_dict": model.state_dict(), "optimizer_state_dict": optimizer.state_dict(), "best_accuracy": best_accuracy}, "model.pth")
		print("new model saved with best accuracy", best_accuracy, "from epoch", epoch+1)

	scheduler.step()
print("best acc", best_accuracy)
