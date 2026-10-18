import torch


a = torch.randint(size=(2,2), low=-10, high=10, dtype=torch.int32)

def bitwise_not(x):
    return ~x

b = torch.flatten(a)
result = torch.vmap(bitwise_not)(b).reshape(2,2)

ref = torch.bitwise_not(a)

assert torch.equal(result, ref)
print("both are equal")
