"""
Take logits of shape (4, 3) and targets = torch.tensor([0, 2, 1, 2]). Use argmax(dim=1) for predictions and print accuracy as (preds == targets).float().mean().

With the same logits and targets, print torch.nn.functional.cross_entropy(logits, targets). Then try passing softmax output instead of raw logits and note how the loss changes.
"""
import torch

logits = torch.randn((4,3))
targets = torch.tensor([0,2,1,2])

preds = torch.argmax(logits, dim=1)
res = preds == targets
print(preds)
print(res.float().mean())

ans1 = torch.nn.functional.cross_entropy(logits, targets)
print(ans1)

ans2 = torch.nn.functional.cross_entropy(torch.softmax(logits, dim=1), targets)
print(ans2)
