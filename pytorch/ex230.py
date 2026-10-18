"""
Write PyTorch code to do create a complex tensor, call conj() on it, then use torch.resolve_conj to produce a tensor with the conjugation resolved (actual values conjugated).
"""

import torch

a = torch.tensor([1+2j],dtype=torch.complex64)
conj_tensor = a.conj()

resolve = torch.resolve_conj(conj_tensor)
