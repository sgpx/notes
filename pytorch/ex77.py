import torch

a = torch.randint(1,10,(2,2))
b = torch.randint(1,10,(2,2))

print(a)
print(b)
print(torch.mm(a,b))
