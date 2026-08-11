"""
write a CNN to detect the number of circles in a monochrome bitmap as an MxN array of 1/0 bits
"""

import random
import torch
import torch.nn as nn
import torch.optim as optim


device = "mps" if torch.mps.is_available() else "cpu"

def bitmap_circle(dim1=320, dim2=240, N=1, radius=5):
    # Initialize a 2D array (dim2 rows by dim1 columns) with 1s (background)
    bitmap = [[1 for _ in range(dim1)] for _ in range(dim2)]

    for _ in range(N):
        # Choose a random center for the circle.
        # Constrained so the circle stays fully inside the boundaries if possible.
        if dim1 > 2 * radius and dim2 > 2 * radius:
            cx = random.randint(radius, dim1 - 1 - radius)
            cy = random.randint(radius, dim2 - 1 - radius)
        else:
            cx = random.randint(0, dim1 - 1)
            cy = random.randint(0, dim2 - 1)

        # Draw the circle outline using the Midpoint Circle Algorithm
        x = radius
        y = 0
        err = 0

        while x >= y:
            # Calculate the points for all 8 octants of the circle
            points = [
                (cx + x, cy + y),
                (cx + y, cy + x),
                (cx - y, cy + x),
                (cx - x, cy + y),
                (cx - x, cy - y),
                (cx - y, cy - x),
                (cx + y, cy - x),
                (cx + x, cy - y),
            ]

            # Plot the points (0 represents a black dot)
            for px, py in points:
                # Boundary check to prevent index out-of-bounds errors
                if 0 <= px < dim1 and 0 <= py < dim2:
                    bitmap[py][px] = 0

            # Update error terms to calculate the next pixel
            if err <= 0:
                y += 1
                err += 2 * y + 1
            if err > 0:
                x -= 1
                err -= 2 * x + 1

    return bitmap


X, Y = [], []
DIMENSION_1 = 320
DIMENSION_2 = 240
NUM_IMAGES = 10000
CIRCLE_MIN_RADIUS = 5
CIRCLE_MAX_RADIUS = 20

for i in range(NUM_IMAGES):
    if i % 1000 == 0 : print("generated", i)
    y = random.randint(1, 10)
    x = bitmap_circle(
        dim1=DIMENSION_1,
        dim2=DIMENSION_2,
        N=y,
        radius=random.randint(CIRCLE_MIN_RADIUS, CIRCLE_MAX_RADIUS),
    )
    X.append(x)
    Y.append(y)

X = torch.tensor(X, dtype=torch.float32, device=device).unsqueeze(1)
Y = torch.tensor(Y, dtype=torch.float32, device=device)


class CircleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(
            in_channels=1, out_channels=16, kernel_size=3, stride=2, padding=1
        )
        self.conv2 = nn.Conv2d(
            in_channels=16, out_channels=32, kernel_size=3, stride=2, padding=1
        )
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(32 * 30 * 22, 64)
        self.fc2 = nn.Linear(64, 1)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.pool(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


dataset = torch.utils.data.TensorDataset(X, Y.unsqueeze(1))

train_size = int(0.8 * NUM_IMAGES)
test_size = NUM_IMAGES - train_size

train_dataset, test_dataset = torch.utils.data.random_split(
    dataset, [train_size, test_size]
)
train_loader = torch.utils.data.DataLoader(train_dataset, shuffle=True, batch_size=32)
test_loader = torch.utils.data.DataLoader(test_dataset, shuffle=False, batch_size=32)

model = CircleCNN()
model = model.to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-5)

NUM_EPOCHS = 100

model.train()
for epoch in range(NUM_EPOCHS):
    print(epoch)
    for X_batch, Y_batch in train_loader:
        X_batch = X_batch.to(device)
        Y_batch = Y_batch.to(device)
        Y_hat = model(X_batch)
        loss = criterion(Y_hat, Y_batch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

model.eval()
with torch.no_grad():
    for X_batch, Y_batch in test_loader:
        X_batch = X_batch.to(device)
        Y_batch = Y_batch.to(device)
        Y_hat = model(X_batch)
        loss = criterion(Y_hat, Y_batch)
        batch_loss = loss.item()
        print(batch_loss)
