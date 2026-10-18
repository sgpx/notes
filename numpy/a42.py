# Write a NumPy script to calculate the Softmax of a 1D array of 10 random integers from scratch, without using any loops.

import numpy as np

a = np.random.randint(0,10,10)
print(a)

def softmax(x):
	n = np.exp(x)
	d = np.sum(n)
	return n/d

res = softmax(a)
