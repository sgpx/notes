"""
Write a PyTorch function attention(Q, K, V) that computes
softmax(Q @ K.T / sqrt(d_k)) @ V using only basic tensor ops. Test it with random tensors of shape (batch, seq, dim).
Stretch: Compare your output against torch.nn.functional.scaled_dot_product_attention to verify correctness.
"""

import torch
import math
import torch.nn.functional as F

batch, seq, dim = 10, 5, 5

def attention(Q,K,V):
	d_k = Q.size(-1)
	scores = Q @ K.transpose(-2, -1)
	scores /= math.sqrt(d_k)
	weights = torch.softmax(scores, dim=-1)
	product = weights @ V
	return product

Q = torch.rand(batch, seq, dim)
K = torch.rand(batch, seq, dim)
V = torch.rand(batch, seq, dim)

output = attention(Q, K, V)
print("Attention:\n", output)

ref = F.scaled_dot_product_attention(Q, K, V)

print(torch.allclose(output, ref))

