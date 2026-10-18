import torch

x = torch.tensor([5,5],dtype=torch.float32, requires_grad=True)
model = torch.nn.Linear(2,1)

prediction = model(x)

print(prediction)

with torch.no_grad():
	prediction =  model(x)
	print(prediction)
