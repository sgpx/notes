"""
Write PyTorch code to do check whether a tensor is CSR sparse with torch.is_sparse_csr and convert a given dense tensor into a torch.sparse_csr_tensor if it isn't.
"""

import torch

# 1. Create a dense tensor
a = torch.randn(5, 6)

# 2. Check if it is CSR sparse using the tensor attribute
print(f"Is 'a' CSR sparse initially? {a.is_sparse_csr}")

# 3. Convert to CSR sparse if it isn't already
if not a.is_sparse_csr:
    b = a.to_sparse_csr()
else:
    b = a

print(f"Is 'b' CSR sparse after conversion? {b.is_sparse_csr}")
