import torch
a = torch.tensor([[1,2],[3,4]], requires_grad=True, dtype=torch.float32)
b = torch.tensor([[4,5],[6,7]], dtype=torch.float32)
c = (a@b).sum()
c.backward()
print(a.grad)
