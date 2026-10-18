import torch 
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_iris

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(4,2)
        self.fc2 = nn.Linear(2, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x



iris = load_iris(as_frame=True)

x = torch.tensor(iris.data.values).float()
y_true = torch.tensor(iris.target.values).float()

model = SimpleNet()

y_pred = model(x)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
loss = criterion(y_pred, y_true)

print(loss.item())
loss.backward()
optimizer.step()
y_pred = model(x)
loss = criterion(y_pred, y_true)
print(loss.item())
