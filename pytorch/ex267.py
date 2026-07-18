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


A = torch.distributions.uniform.Uniform(-1, 1).sample((1000, 2, 2))
det = torch.abs(A[:,0,0] * A[:,1,1] - A[:,0,1]*A[:,1,0])
mask = det > 0.1
A = A[mask]
print(A.shape)
A_inv = torch.linalg.inv(A)
num_samples = A.shape[0]
A = A.reshape(num_samples, 4)
A_inv = A_inv.reshape(num_samples, 4)

A_train, A_test = torch.data.utils.random_split(A, [0.8, 0.2])
A_inv_train, A_inv_test = torch.data.utils.random_split(A_inv, [0.8, 0.2])


print(A_train, A_test)
