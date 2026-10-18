import torch

a = torch.tensor([ [1,2], [3,4] ])

b = torch.transpose(a, 1, 0)

print(a)
print(b)
