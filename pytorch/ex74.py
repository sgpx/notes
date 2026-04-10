import torch

a = torch.tensor([1,2])
b = torch.tensor([3,4])

result = torch.cat((a,b),dim=0)

print(a)
print(b)
print(result)

print("===")

a = torch.randint(1,10, (2,2))
b = torch.randint(1,10, (2,2))

result = torch.cat((a,b),dim=0)

print(a)
print(b)
print(result)

print("===")
result = torch.cat((a,b),dim=1)
print(result)
