"""
**Question:**  
You have a batch of data `X` with shape `(32, 10)` (32 samples, each 10 features), and a linear layer with weights `W` of shape `(10, 5)` and bias `b` with shape `(5,)` in PyTorch.

Write a single line of code to compute the output tensor `Y` (i.e., the result after applying the linear layer and adding bias), ensuring correct broadcasting and shape. What will be the shape of `Y`? Also, explain in one short sentence *why* broadcasting works in your code.

---

Please answer in the format:  
1. The code line (PyTorch syntax)  
2. The resulting shape of `Y`  
3. One-sentence explanation of how bias broadcasting works here
"""

import torch
X = torch.rand(32, 10, dtype=torch.float32)
W = torch.rand(10, 5, dtype=torch.float32)
b = torch.rand(5, dtype=torch.float32)

Y = (X@W) + b

print(Y, Y.shape)

"""
Answer:

Y = (X@W) + b # X@W is 32x10 * 10x5 => 32x5, b is a 1D tensor of shape 5, it gets broadcasted across all 32 columns so the end result is a 32x5 matrix + 32x5 matrix = 32x5
"""
