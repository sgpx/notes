import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(10, 5)  # Input layer: 10 features to 5 neurons
        self.relu = nn.ReLU()         # Activation
        self.fc2 = nn.Linear(5, 2)   # Output layer: 5 neurons to 2 classes
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Creating an instance and passing some dummy data
model = SimpleNN()
input_tensor = torch.randn(3, 10)  # batch of 3 samples, each with 10 features
output = model(input_tensor)
print(output)
