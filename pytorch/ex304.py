"""
Take logits of shape (4, 3) and targets = torch.tensor([0, 2, 1, 2]). Use argmax(dim=1) for predictions and print accuracy as (preds == targets).float().mean().
"""
import torch

logits = torch.randn((4,3))
targets = torch.tensor([0,2,1,2])

preds = torch.argmax(logits, dim=1)
res = preds == targets
print(preds)
print(res.float().mean())
