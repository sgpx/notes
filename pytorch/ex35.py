import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

# Define your model
class SmallNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(20, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 2)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

# Generate dummy data
num_samples = 1000
feature_dim = 20
data = torch.randn(num_samples, feature_dim)
labels = torch.randint(0, 2, (num_samples,))

# Create dataset and dataloader
dataset = TensorDataset(data, labels)
batch_size = 32
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Instantiate model, loss function, and optimizer
model = SmallNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())

# Training loop for 5 epochs
for epoch in range(5):
    total_loss = 0.0  # Initialize total loss for the epoch
    for inputs, targets in dataloader:
        # Forward pass: compute predictions
        outputs = model(inputs)
        
        # Compute cross-entropy loss
        loss = criterion(outputs, targets)
        
        # Backward pass: compute gradients
        loss.backward()
        
        # Optimizer step: update model parameters
        optimizer.step()
        
        # Zero gradients for next iteration
        optimizer.zero_grad()
        
        # Accumulate loss
        total_loss += loss.item()
    
    # Compute and print average loss for the epoch
    avg_loss = total_loss / len(dataloader)
    print(f"Epoch [{epoch+1}/5], Average Loss: {avg_loss:.4f}")