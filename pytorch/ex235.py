"""
Write PyTorch code to do elementwise compute the next representable float of tensor a toward tensor b using torch.nextafter.
"""

import torch
b = torch.randn(5,5)
a = torch.randn(5,5)
print(torch.nextafter(a,b))


