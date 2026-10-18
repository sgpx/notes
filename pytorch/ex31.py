import torch
from torchviz import make_dot

x = torch.tensor([2.0, 3.0], requires_grad=True)
y = x**2 + 3*x + 1
z = y.sum()

dot = make_dot(z, params={'x': x})
dot.render("computational_graph", format="png")
