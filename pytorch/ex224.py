"""
Write PyTorch code to do elementwise ceiling on a 2x3 float tensor, reshape it to 3x2, and convert the result to a torch.LongTensor.
"""

import torch 
a = torch.ceil(torch.rand(2,3, dtype=torch.float32))
b = a.reshape(3,2) 
c = torch.LongTensor(b.to(torch.long)) 
print(c)
