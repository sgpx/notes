import torch
import numpy as np

np_arr = np.array([1,2,3])
torch_tensor = torch.from_numpy(np_arr)

print(np_arr)
print(torch_tensor)

np_arr[0] = 10


print(np_arr)
print(torch_tensor)

torch_tensor[2] = 99


print(np_arr)
print(torch_tensor)

np_arr = np.array([[1,2],[3,4]])
torch_tensor = torch.from_numpy(np_arr)

print(np_arr)
print(torch_tensor)

print(np_arr[1,1])
print(torch_tensor[1,1])

torch_tensor[1,1] = 456

print(np_arr)
print(torch_tensor)

np_arr = np.array([[1,2],[3,4]], dtype=np.float32)
torch_tensor = torch.from_numpy(np_arr)

print(np_arr)
print(torch_tensor)

np_arr = np.array([[1,2],[3,4]], dtype=np.float64)
torch_tensor = torch.from_numpy(np_arr)

print(np_arr)
print(torch_tensor)
