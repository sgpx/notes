# Normalize a 5x5 random matrix (i.e., subtract the mean and divide by the standard deviation).

import numpy as np

a = np.random.rand(5,5)
b = np.mean(a)
c = np.std(a)
print(a, b)
a -= b
a /= c
print(c)
print(a)
