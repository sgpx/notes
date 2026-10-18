##Next Topic:## Learn about NumPy's ##broadcasting## in more depth.

##Challenging Problem:## Write a function that takes a 3D NumPy array and a 1D array of weights, then applies the weights to each slice of the 3D array (along the first axis) through broadcasting. Your function should return the modified 3D array.

##What to Learn:## Familiarize yourself with how broadcasting works in NumPy, especially in terms of aligning shapes for arithmetic operations.

import numpy as np

def fxn(a,w):
	return a*w


a = np.random.randint(1,5, (3,3, 3))
w = np.random.randint(1,5, (3))
print(a,w,fxn(a,w))
