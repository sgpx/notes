"""
Create a 1D tensor of 5 random floats. Implement the SiLU (Swish) activation function manually by multiplying the tensor by its sigmoid (x * torch.sigmoid(x)). Compare your result to torch.nn.functional.silu using torch.allclose.
"""
import torch
a = torch.rand(5, dtype=torch.float32)


swish = lambda x : x * torch.sigmoid(x)

b = swish(a)
c = torch.nn.functional.silu(a)

print(torch.allclose(b,c))
