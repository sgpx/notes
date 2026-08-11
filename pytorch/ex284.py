import torch

a = torch.randint(size=(10,3), low=1, high=11, dtype=torch.int32)
print(a, a.shape)
b = torch.randint(size=(10,1), low=1, high=11, dtype=torch.int32)
print(b, b.shape)

c = torch.hstack([a,b])
print(c)

