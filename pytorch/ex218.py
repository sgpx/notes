"""

pytorch code to do bitwise OR with a 3x1 tensor vs a 1x4 tensor of int32 dtype with broadcasting

"""

import torch

a = torch.randint(size=(3,1), dtype=torch.int32, high=10, low=1)
b = torch.randint(size=(1,4), dtype=torch.int32, high=10, low=1)

c = a | b

print(c)
