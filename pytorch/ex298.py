"""
Task: Instantiate a minimal nn.Linear(2, 2) layer, manually assign large values to its gradients using model.weight.grad = torch.full_like(model.weight, 50.0), and invoke torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0).   
TXT
Objective: Calculate and print the Euclidean norm of the gradient tensor before and after clipping to observe how exploding gradients are scaled down in place
"""

import torch
import torch.nn as nn

model = nn.Linear(2,2)

model.weight.grad = torch.full_like(model.weight, 50.0)
print(torch.norm(model.weight.grad))

nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
print(torch.norm(model.weight.grad))


