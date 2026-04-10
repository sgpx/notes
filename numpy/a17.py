##Next Topic: NumPy Sorting and Searching##

##Challenging Problem:## Create a function that takes a 2D NumPy array and returns both the row indices and column indices of the largest `n` elements in the array, along with their values. Implement this for `n = 3`.

import numpy as np

a = np.random.randint(0,10,(4,4))

minus_inf = float('-inf')
b = [minus_inf]*3
c = [None, None, None]

for n,i in enumerate(a):
	for m,j in enumerate(i):
		for k in range(2,-1,-1):
			if b[k] <= j:
				b = [j] + b[:-1]
				c = [(n,m)] + c[:-1]
				break


print(a)
print(b)
print("loc:",c)
