import torch

num_samples = 10
m = 2
x = torch.randn(num_samples, 1)


b = torch.randn(num_samples, 1) * 0.1

y = (m*x) + b

torch.save(y,"foo.pt")

y2 = torch.load("foo.pt")

print(y2)
