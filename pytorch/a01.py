import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
torch.manual_seed(0)

# 1. Generate Synthetic Data
# We create a linear relationship with some noise
x = np.random.rand(100, 1) * 10  # 100 samples, 1 feature
true_slope = 2.0
true_intercept = 5.0
y = true_slope * x + true_intercept + np.random.randn(100, 1)  # Add some noise

# Convert to PyTorch tensors
X = torch.FloatTensor(x)
Y = torch.FloatTensor(y)

# 2. Define the Linear Regression Model
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # 1 input, 1 output

    def forward(self, x):
        return self.linear(x)

# Initialize the model
model = LinearRegressionModel()

# 3. Define Loss Function and Optimizer
criterion = nn.MSELoss()  # Mean squared error loss
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic gradient descent

# 4. Train the Model
num_epochs = 1000
for epoch in range(num_epochs):
    model.train()
    
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, Y)
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 100 == 0:  # Print every 100 epochs
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# 5. Visualizing the results
model.eval()
with torch.no_grad():
    predicted = model(X).detach().numpy()

plt.scatter(x, y, label='Original data')
plt.plot(x, predicted, label='Fitted line', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression with PyTorch')
plt.legend()
plt.show()