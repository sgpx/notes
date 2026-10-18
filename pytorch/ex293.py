"""
Construct a minimal Multi-Head Attention module (nn.Module) extending your scaled dot-product attention work

Set d_model = 64 and heads = 4 (d_k = 16).

In forward(x): project input X of shape (batch, seq_len, d_model), reshape and transpose to (batch, heads, seq_len, d_k), pass to torch.nn.functional.scaled_dot_product_attention, re-transpose/flatten, and project through W_O

Pass a random tensor with shape (2, 8, 64) and verify that the output shape is exactly (2, 8, 64)
"""

d_model = 64
heads = 4
d_k = 16


