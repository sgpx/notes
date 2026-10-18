"""
Write an exact 4-line PyTorch script that initializes a weight matrix W of shape (4,4) with random numbers, separates W into low-rank factor tensors A of shape (4,1) and B of shape (1,4) (both initialized to ones with tracking enabled), adds the product AB to the base weight W to form a composite weight W_updated, and computes the backward pass of the sum of W_updated
"""


import torch
W,A,B = torch.rand(4,4,dtype=torch.float32), torch.ones(4,1,requires_grad=True), torch.ones(1,4,requires_grad=True)
A,B = W[:,1].clone().unsqueeze(1).requires_grad_(),W[1,:].clone().unsqueeze(0).requires_grad_(),
W_upd = (A@B) + W
W_upd.sum().backward()
