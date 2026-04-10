import torch
import numpy as np

np_arr = np.array(np.random.randn(5,1) * 100, dtype=np.int32)
print(np_arr)
torch_tensor = torch.from_numpy(np_arr)

print(torch.mean(torch_tensor, dtype=torch.float32))
