import torch

for i in [torch.float16, torch.float32, torch.float64]:
	for j in [torch.float16, torch.float32, torch.float64]:
		if i == j: continue
		a = torch.tensor([1.5,2.5], dtype=i)
		b = torch.tensor([3.4,1.4], dtype=j)

		print(a, i)
		print(b, j)
		print(a+b)
		
