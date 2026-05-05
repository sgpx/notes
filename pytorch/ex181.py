import torch
import os

os.chdir("ex181data")

print(os.system("ls"))

for i in range(1,5):
	for j in os.listdir(f"l{i}"): # l1, l2, l3, l4 => folders containing labeled data
		pass		

class mydataclass(torch.utils.data.Dataset):
	def __init__(self, data): self.data = data
	def __len__(self): return len(self.data)
	def __getitem__(self, index): return self.data[index]


class FNN(torch.nn.Module):
	def __init__(self):
		super().__init__()
		self.p1 = torch.nn.Conv2D(512,64)
		self.p2 = torch.nn.MaxPool2D(64,16)
		self.p3 = torch.nn.Conv2D(16, 4)
		self.relu = torch.nn.ReLU(inplace=True)

	def forward(self, x):
		x = self.p1(x)
		x = self.p2(x)
		x = self.relu(x)
		x = self.p3(x)



dataset = mydataclass(prep())
loader = torch.data.utils.DataLoader(dataset, shuffle=True, batch_size=8)

model = FNN()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(100):
	for x_batch, y_batch in loader:
		optimizer.zero_grad()
		y_hat = model(y_batch)
		loss = torch.nn.MSELoss(y_hat, y_batch)
		optimizer.step()
		loss.backward()	

