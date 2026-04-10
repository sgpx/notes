#**Challenging Problem:** Given a 5x5 NumPy array filled with random integers from 0 to 100, write a function to find the largest 2x2 sub-array. Print both the sub-array and its sum.

import numpy as np

a = (np.random.rand(5,5)*100).astype(int)

print(a)


print(a.shape)

arr = None
ars = float("-inf")
for i in range(a.shape[0] - 1):
	for j in range(a.shape[1] - 1):
		rs, re = i, i+2
		cs, ce = j, j+2
		rv = a[rs:re, cs:ce]
		rs = np.sum(rv)
		if rs > ars:
			ars = rs
			arr = rv


print(arr)
print(ars)
