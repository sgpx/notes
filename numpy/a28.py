import numpy as np

arr = np.random.randn(3,3) * 100
arr = np.ceil(arr)
print(arr)

e_val, e_vec = np.linalg.eig(arr)

print(arr)
print(e_vec)
