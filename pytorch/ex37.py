import torch 
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

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
model = SimpleNet()

X = torch.tensor(iris.data.values).float()
y = torch.tensor(iris.target.values).float()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


X_train = torch.tensor(X_train).float()
y_train = torch.tensor(y_train).float()
X_test = torch.tensor(X_test).float()
y_test = torch.tensor(y_test).float()

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

epochs = 100

for epoch in range(epochs):
        y_pred = model(X_train)
        loss = criterion(y_pred, y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch+1 % 20 == 0:
                print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

def evaluate_accuracy(model, X, y, set_name):
        with torch.no_grad():
                outputs = model(X)
                _, predicted = torch.max(outputs, 1)
                accuracy = (predicted == y).sum().item() / y.size(0)
                print(f'{set_name} Accuracy: {accuracy * 100:.2f}%')

print("--- Evaluation ---")
evaluate_accuracy(model, X_train, y_train, "Train")
evaluate_accuracy(model, X_test, y_test, "Test")
