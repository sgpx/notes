import numpy as np

a = (np.random.rand(5,5)*100).astype(int)

print(a)

b = a[1:4 , 1:4]
print(b)
