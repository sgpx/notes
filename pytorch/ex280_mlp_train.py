import json
import torch
import torch.nn as nn
import torch.optim as optim

NUM_EPOCHS = 20
EMB_DIMS = 1536
EMBEDDING_MODEL = "text-embedding-3-small"
raw_data = json.loads(open("ex280_lv4.json", "r").read())
raw_data = [i for i in raw_data if i.get("embeddings")]
X = torch.tensor([i["embeddings"][EMBEDDING_MODEL] for i in raw_data], dtype=torch.float32)
X = X.to("mps")
Y = torch.tensor([1 if i.get("is_music") else 0 for i in raw_data], dtype=torch.float32)
Y = Y.to("mps")


class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(EMB_DIMS, 3000)
        self.fc2 = nn.Linear(3000, 1000)
        self.fc3 = nn.Linear(1000, 100)
        self.fc4 = nn.Linear(100, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        x = self.relu(x)
        x = self.fc4(x)
        return x

model = SimpleNN().to("mps")
optimizer = optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.BCEWithLogitsLoss()

dataset = torch.utils.data.TensorDataset(X, Y)
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [0.8, 0.2])

train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=16, shuffle=True
)
test_loader = torch.utils.data.DataLoader(
    test_dataset, batch_size=16, shuffle=False
)

model.train()
for epoch in range(NUM_EPOCHS):
    #print("epoch:", epoch)
    for X_batch, Y_batch in train_loader:
        Y_pred = model(X_batch)
        loss = criterion(Y_pred, Y_batch.unsqueeze(1))
        optimizer.zero_grad()
        loss.backward()
        #print("batch loss: ", loss.item())
        optimizer.step()

model.eval()
with torch.no_grad():
	total_loss, ctr = 0, 0
	for X_batch, Y_batch in test_loader:
		Y_pred = model(X_batch)
		loss = criterion(Y_pred, Y_batch.unsqueeze(1))
		batch_loss = loss.item()
		#print("batch loss:", batch_loss)
		total_loss += batch_loss
		ctr += 1
	#print("total loss:", total_loss/ctr)

torch.save(model.state_dict(), "ex280_lv4.pt")

