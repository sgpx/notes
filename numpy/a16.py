##Next Topic##: NumPy Advanced Indexing

##Challenge##: Given a 3D NumPy array of shape (3, 4, 5), extract a specific 2x2 slice from each 2D array along the first axis, and compute the sum of all the extracted slices.

import numpy as np

a = np.random.randint(0,100,(3,4,5))
#print(a)

for i in a:
	slice = i[0:2,0:2]
	print(i, slice)
	print(np.sum(slice))
	print("===")
