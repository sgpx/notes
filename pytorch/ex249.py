# Use torch.nn.functional.one_hot to convert class indices to one‑hot vectors and shows how to feed them into a model.

import torch

N = 1000

"""
telco_customer_labels = {
	0: "landline",
	1: "mobile",
	2: "broadband",
	3: "cable"
}
"""

customer_type_indices = torch.randint(size=(N,), low=0, high=4)
customer_onehot = torch.nn.functional.one_hot(customer_type_indices, num_classes=4)
postpaid = torch.randint(size=(N,), low=0, high=2)
print(postpaid)
last_three_bills = torch.randint(size=(N,3), low=10, high=200)

def churn_simulator(row): # make some fake data
	bills = row[-3:]
	postpaid_flag = row[4].to(dtype=torch.bool)
	a2 = (torch.sum(bills) / 3) > 150
	a2 = a2.to(dtype=torch.bool)
	return (postpaid_flag & a2)

data = torch.hstack([customer_onehot, postpaid.unsqueeze(1), last_three_bills])
data = data.to(dtype=torch.float32)
is_churned = torch.vmap(churn_simulator)(data)

print(data)
print(is_churned)
y_true = is_churned.to(dtype=torch.float32)

class SimpleNN(torch.nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = torch.nn.Linear(8, 4)
		self.relu = torch.nn.ReLU()
		self.fc2 = torch.nn.Linear(4, 1)

	def forward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.fc2(x)
		return x

model = SimpleNN()
criterion = torch.nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

NUM_EPOCHS = 1000

for epoch in range(NUM_EPOCHS):
	y_hat = model(data)
	loss = criterion(y_hat.squeeze(), y_true)
	optimizer.zero_grad()
	loss.backward()
	optimizer.step()
	print(epoch, loss.item())

with torch.no_grad():
	model.eval()
	x_test = torch.tensor([0, 1, 0, 0, 1, 150, 120, 130], dtype=torch.float32)
	logit = model(x_test.unsqueeze(0))
	probability = torch.sigmoid(logit)  # Convert logit to probability
	print(f"Logit: {logit.item():.4f}")
	print(f"Probability: {probability.item():.4f}")
