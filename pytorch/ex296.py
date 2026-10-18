"""
### Problem: Weighted Row Aggregation with Autograd

Given an input tensor $X$ and a learnable weighting vector $w$, compute a weighted row sum, calculate the scalar Mean Squared Error against a target value, and backpropagate to find the gradient with respect to $w$.

#### Task Requirements

1. Create a 2D tensor `X` of shape `(3, 4)` initialized with values from $1.0$ to $12.0$ (`float32`).
2. Create a 1D tensor `w` of length $4$ containing all ones, with gradient tracking enabled (`requires_grad=True`).
3. Compute the weighted element-wise product `Y = X * w` using broadcasting.
4. Sum `Y` across the last dimension (`dim=1`) so each row is collapsed into a single scalar, yielding a tensor of shape `(3,)`.
5. Compute a scalar loss: the Mean Squared Error between the row sums and a target tensor `target = torch.tensor([10.0, 20.0, 30.0])`.
6. Run `loss.backward()` and print `w.grad` along with the scalar `loss.item()`.


"""
import torch

X = torch.arange(1, 12+1).reshape(3,4).to(dtype=torch.float32)
w = torch.ones(4, requires_grad=True, dtype=torch.float32)
row_sums = torch.sum(X * w, dim=1)

target = torch.tensor([10.0, 20.0, 30.0])

loss = torch.mean((target - row_sums)**2)


loss.backward()
print(w.grad)
print(row_sums, target)
print(loss.item())

