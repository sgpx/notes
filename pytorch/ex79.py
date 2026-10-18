import torch

a = torch.tensor([1,2,3],dtype=torch.float64)

print(a.requires_grad)
print(a.requires_grad_())

b = torch.tensor([4,5,6], requires_grad=True, dtype=torch.float64)

print(b.requires_grad)

print(b.requires_grad_())
