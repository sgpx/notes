"""
Write PyTorch code to do create two tensors a and b with identical numeric values but different dtypes, show torch.equal returns False, then cast one to the other's dtype and show torch.equal returns True.
"""

import torch

a = torch.tensor([1,2,4], dtype=torch.int32)
b = torch.tensor([1,2,4], dtype=torch.float32)

print(torch.equal(a,b))
print(torch.equal(a,b.type_as(a)))
