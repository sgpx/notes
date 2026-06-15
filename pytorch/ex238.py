# Write PyTorch code to do create a tensor with values 0..5 of dtype torch.float32, cast it to torch.int64, reshape to (3,2), and transpose it.

import torch
a = torch.arange(0,5+1,dtype=torch.float32)
b = a.to(dtype=torch.int64)
b = b.reshape(3,2)
print(b.T)
