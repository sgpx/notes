"""
Write an exact 3-line PyTorch script that creates a random 4×4 tensor T, transposes it using .t(), and then attempts to flatten it using .view(-1). Fix the runtime error that this sequence naturally causes without changing the shape or using .reshape().
"""

import torch
print(torch.rand(4,4).t().contiguous().view(-1))
