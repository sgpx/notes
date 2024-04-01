1. Beginner:
    1. Install numpy and print its version.

```
from numpy.version import full_version
print(full_version)
```

    2. Create a numpy array of size 10, filled with zeros.

```
import numpy
a = numpy.array([0]*10)
print(a)
```

    3. Create a numpy array with values ranging from 10 to 50.

```
import numpy
a = numpy.array([i for i in range(10,51)])
```

    4. Reverse the numpy array you've created.

```
import numpy
a = numpy.array([i for i in range(10,51)])
b = a[::-1]
```

    5. Create a 3x3 matrix with values ranging from 0 to 8.

```
import numpy as np
a = np.arange(9).reshape(3,3)
print(a)
```

```
>>> import numpy as np
>>> from random import randint
>>> a = np.array([[randint(0,8) for i in range(3)] for _ in range(3)])
>>> a
array([[3, 8, 3],
       [1, 5, 0],
       [7, 0, 4]])
>>> a.size
9
>>> a.shape
(3, 3)
```

2. Intermediate:
    6. Create a 5x5 array with 1's on the border and 0 inside.


```

```
    7. Multiply a 5x3 matrix by a 3x2 matrix.
    8. Create a random array of 30 and find the average.
    9. Swap two rows in a 2D numpy array.
    10. Find the most frequent value in a numpy array.

3. Advanced:
    11. Create a 2D array of shape 5x5 and convert it to a 1D array.
    12. Compute the sum of all elements, sum of each column and sum of each row of a given array.
    13. Normalize a 5x5 random matrix (i.e., subtract the mean and divide by the standard deviation).
    14. Write a function to find moving average over an array.
    15. Given an array of random integers, make an array where each element is its rank, i.e., replace the element with its rank when sorted.


