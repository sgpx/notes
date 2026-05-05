import torch
import sys
import time

device_name = sys.argv[-1]

TENSOR_DIM = int(sys.argv[-2])

st = time.time()
a = torch.rand(TENSOR_DIM, TENSOR_DIM, dtype=torch.float32, device=device_name)
b = torch.rand(TENSOR_DIM, TENSOR_DIM, dtype=torch.float32, device=device_name)

c = torch.matmul(a, b)

if device_name == "mps": torch.mps.synchronize()

ts = time.time() - st

print(f"dim: {TENSOR_DIM}x{TENSOR_DIM}")
print(device_name)
print("time taken: ", ts, "Seconds")
