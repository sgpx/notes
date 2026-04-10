Sure! Here's a simple learning problem suitable for practicing `torch.nn.Linear`.

---

### Problem: Predict a linear relationship

**Goal:** Given an input feature `x`, predict the output `y` where `y` is linearly related to `x` as:

\[ y = 2x + 1 \]

---

### Step-by-step:

1. **Generate some data:**

```python
import torch

# Create input data
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # shape: (100, 1)

# Generate target data based on the linear rule y = 2x + 1 + noise
y = 2 * x + 1 + 0.2 * torch.randn(x.size())
```

2. **Define a model using `torch.nn.Linear`:**

```python
import torch.nn as nn

model = nn.Linear(in_features=1, out_features=1)
```

3. **Set up a loss function and optimizer:**

```python
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
```

4. **Train the model:**

```python
for epoch in range(100):
    # Forward pass
    y_pred = model(x)
    
    # Compute loss
    loss = criterion(y_pred, y)
    
    # Zero gradients, perform backward pass, and update weights
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')
```

5. **Check the learned parameters:**

```python
print(f'Learned weight: {model.weight.item():.2f}')
print(f'Learned bias: {model.bias.item():.2f}')
```

---

### Summary:

This simple example uses `torch.nn.Linear` to learn the relationship `y = 2x + 1` from noisy data. After training, the model should approximate the coefficients `2` and `1`.

Feel free to experiment with the number of epochs, learning rate, or data!
