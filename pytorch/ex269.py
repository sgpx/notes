# Write a PyTorch script to manually compute a single gradient descent update step for the function J(θ)=θ^2 +4θ without using .backward().

import torch

J = lambda theta : (theta**2) + (4*theta)

x = torch.tensor(3.0, requires_grad=True)

val = J(x)

dJ_dtheta = lambda theta : (2*theta) + 4


grad = dJ_dtheta(x)
lr = 0.01
print(x)
print(J(x))
print(grad)
with torch.no_grad(): # disable graph tracking for update step
	x = x - lr*grad
print(x)
