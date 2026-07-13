"""
Write PyTorch code to do set columns 0 and 2 of a torch.zeros(3,4) tensor to the value 5 using torch.index_fill along dim=1.
"""

import torch
a = torch.zeros(3,4)
b = torch.index_fill(a, value=5, dim=1, index=torch.tensor([0,2]))
print(b)
