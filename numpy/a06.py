import numpy as np
a = np.arange(1,17)
a = np.flip(a,axis=0)
a = a.reshape((4,4))
print(a)

b = np.flip(np.arange(1,17).reshape((4,4)), axis=1)
print(b)
