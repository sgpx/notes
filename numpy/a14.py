#Topic:# NumPy Masking and Filtering

#Challenge:# Create a function that takes a 5x5 NumPy array filled with random integers and returns a new array containing only the even numbers. Also, compute the sum of the numbers in the new array.

import numpy as np
a = np.random.randint(0, 20, (5,5))
print(a)

mask1 = a % 2 == 0

f1 = a[mask1]

print(f1)
print(np.sum(f1))
