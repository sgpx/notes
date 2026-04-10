import torch

x = torch.tensor(1.0, dtype=torch.float64, requires_grad=True)
w = torch.tensor(2.0, dtype=torch.float64, requires_grad=True)
b = torch.tensor(5.0, dtype=torch.float64, requires_grad=True)

y = x * w + b

y.backward()

print("dy/dx:", x.grad)  # gradient of y w.r.t x
print("dy/dw:", w.grad)  # gradient of y w.r.t w
print("dy/db:", b.grad)  # gradient of y w.r.t b
