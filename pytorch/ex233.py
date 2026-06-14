"""
Write PyTorch code to do the bitwise NOT of a given integer tensor without calling torch.bitwise_not, and verify the result equals torch.bitwise_not(tensor).
"""

import torch


a = torch.randint(size=(2,2), low=-10, high=10, dtype=torch.int32)
result = ~a

ref = torch.bitwise_not(a)

assert torch.equal(result, ref)
print("both are equal")

