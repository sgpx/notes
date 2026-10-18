import gc
import torch
import time

ts1 = time.time()
N = 10000*2

a = torch.randn(N,N,device="cpu")
b = torch.randn(N,N,device="cpu")

c = torch.sum(a @ b)

ts2 = time.time()

print("cpu time", ts2 - ts1)
print(f"The sum is: {c.item()}")

del a
del b
del c

gc.collect()

ts1 = time.time()

a = torch.randn(N,N,device="mps")
b = torch.randn(N,N,device="mps")

c = torch.sum(a @ b)


torch.mps.synchronize()
# 3. BLOCK the CPU until the GPU is actually finished

ts2 = time.time()

print(f"The sum is: {c.item()}")

print("gpu time", ts2 - ts1)
