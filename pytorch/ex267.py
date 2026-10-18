"""
Problem idea:
- Learn a function f that maps a small invertible matrix A to its inverse A⁻¹. That is, f: R^{n×n} → R^{n×n}, aiming to approximate A⁻¹.
- Start with n = 2 for simplicity (flatten matrices to vectors). You’ll train a network to take the 4 entries of A and output the 4 entries of A⁻¹.

Why this is easy:
- The input/output are small fixed-size vectors, so a tiny feedforward network suffices.
- You can generate unlimited training data by sampling random 2×2 invertible matrices and computing their inverses exactly.
- It’s a supervised learning setup: you have ground-truth A⁻¹ for every A.

Steps to implement:

1) Data generation
- Sample A = [[a, b], [c, d]] with a, b, c, d drawn from Uniform(-1, 1).
- Reject A if abs(det(A)) is too small (to avoid ill-conditioning). For example, require |ad - bc| > 0.1.
- Compute A⁻¹ analytically (or with a numerical tool). Let A_inv = inv(A).
- Create a dataset pair: input X = [a, b, c, d], target y = [A_inv[0,0], A_inv[0,1], A_inv[1,0], A_inv[1,1]].
- Normalize inputs/outputs if desired (e.g., scale to [-1, 1]).

2) Model design
- Use a small multilayer perceptron (MLP).
  - Input size: 4
  - Hidden layers: e.g., 2 layers with 64 units each and ReLU activations
  - Output size: 4
- Loss: mean squared error (MSE) between predicted A⁻¹ and true A⁻¹.
- Optional regularization: weight decay (L2).

3) Training procedure
- Split into train/validation/test sets (e.g., 70/15/15).
- Optimizer: Adam with learning rate around 1e-3.
- Mini-batch size: 32–128
- Train until validation loss stops improving (early stopping).

4) Evaluation
- On the test set, report:
  - Relative Frobenius error: ||A⁻¹ - ŜA⁻¹||_F / ||A⁻¹||_F
  - Or average MSE per element
- Optional sanity check: compute A @ ŜA⁻¹ and compare to I (should be close to identity).

5) Extensions (optional)
- Use n = 3 (9 inputs, 9 outputs) for a bigger challenge.
- Instead of direct A⁻¹ output, train a network to solve Ax = b:
  - Provide A and b as inputs, train to output x = A⁻¹ b.
  - This tests the model’s ability to perform linear system solving in a learned way.
- Add a consistency term to the loss: minimize ||A·ŜA⁻¹ − I||_F as a secondary objective, encouraging the predicted inverse to satisfy the defining property A·A⁻¹ = I.
- Try conditioning-aware sampling: sample matrices with a range of condition numbers to study how conditioning affects learning.

Starter pseudocode (high level, Python-like):

- Data generation:
  for i in range(N):
      A = random_uniform_matrix(2, 2, range=(-1, 1))
      if abs(det(A)) <= 0.1:
          continue
      A_inv = inverse(A)
      X[i] = flatten(A)
      Y[i] = flatten(A_inv)

- Model (Keras-like, outline):
  model = Sequential([
      InputLayer(input_shape=(4,)),
      Dense(64, activation='relu'),
      Dense(64, activation='relu'),
      Dense(4)
  ])
  model.compile(optimizer='adam', loss='mse')
  model.fit(X_train, Y_train, validation_data=(X_val, Y_val), epochs=100, batch_size=64)

- Evaluation:
  Y_pred = model.predict(X_test)
  error = FrobeniusNorm(A_inv_test - Y_pred) / FrobeniusNorm(A_inv_test)

What you’ll learn from this exercise:
- Deep networks can approximate nonlinear mappings like matrix inversion on small scales.
- The quality of approximation depends on matrix conditioning; very ill-conditioned A can make learning harder.
- It’s a good demo of “learn a function that is known analytically” and then compare to exact computation.

"""
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, random_split, DataLoader

def relative_frobenius_error(Y_true, Y_pred, eps=1e-12):
    # Y_* are (B,4). reshape to (B,2,2)
    Bt = Y_true.shape[0]
    Y_true_m = Y_true.reshape(Bt, 2, 2)
    Y_pred_m = Y_pred.reshape(Bt, 2, 2)

    num = torch.linalg.norm(Y_true_m - Y_pred_m, ord='fro', dim=(1,2))
    den = torch.linalg.norm(Y_true_m, ord='fro', dim=(1,2))
    return (num / (den + eps)).mean().item()

A = torch.distributions.uniform.Uniform(-1, 1).sample((1000, 2, 2))
det = torch.abs(A[:,0,0] * A[:,1,1] - A[:,0,1]*A[:,1,0])
mask = det > 0.1
A = A[mask]
print(A.shape)
A_inv = torch.linalg.inv(A)
num_samples = A.shape[0]
A = A.reshape(num_samples, 4)
A_inv = A_inv.reshape(num_samples, 4)
X = A
Y = A_inv

dataset = TensorDataset(X, Y)
train_size = int(0.8*len(dataset))
test_size = len(dataset) - train_size

tv_set, test_set = random_split(dataset, [train_size, test_size])

train_size = int(0.8*len(tv_set))
test_size = len(tv_set) - train_size
train_set, validation_set = random_split(tv_set, [train_size, test_size])

train_loader = DataLoader(train_set, batch_size=32)
test_loader = DataLoader(test_set, batch_size=32)
validation_loader = DataLoader(validation_set, batch_size=32)

class SimpleNN(nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(4, 64)
		self.fc2 = nn.Linear(64, 32)
		self.fc3 = nn.Linear(32, 4)
		self.relu = nn.ReLU()

	def forward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.fc2(x)
		x = self.relu(x)
		x = self.fc3(x)
		return x

model = SimpleNN()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
criterion = nn.MSELoss()

NUM_EPOCHS = 100

model.train()
for epoch in range(NUM_EPOCHS):
	for X_batch, Y_batch in train_loader:
		optimizer.zero_grad()
		pred = model(X_batch)
		loss = criterion(pred, Y_batch)
		loss.backward()
		optimizer.step()
		print(epoch, loss.item())

model.eval()

with torch.no_grad():
	for X_batch, Y_batch in test_loader:
		pred = model(X_batch)		
		test_loss = criterion(pred, Y_batch)
		print(test_loss.item())

	
