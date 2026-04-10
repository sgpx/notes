##Next Topic:## Learn about NumPy's ##advanced indexing## techniques that allow you to manipulate and select data in more complex ways.

##Challenging Problem:## Write a function that takes a 2D NumPy array and an array of row indices and column indices, then returns the corresponding elements from the array. For example, if given the array `arr` and lists of indices `rows = [0, 2]` and `cols = [1, 3]`, your function should return `arr[0,1]` and `arr[2,3]`.

##Learning Resource:## Familiarize yourself with NumPy's advanced indexing and the concept of using integer arrays for indexing.

import numpy as np

def fxn(a, r, c):
	return a[r,c]

a = np.random.randint(1,5,(3,3))
r = np.array([0,1,2])
c = np.array([1,1,1])

print(a, fxn(a,r,c))
