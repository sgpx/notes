# numpy

`pip3 install numpy`

# array

```
import numpy as np
a = np.array([2,3,4,5])
print(a.size)
print(a.shape)
print(a.sum)

b = np.array([5,6,7,8])
c = a+b
print(c)
print(c[-1])
print(c[1:3])
```

# arange

```
>>> import numpy as np
>>> a = np.arange(5)
>>> a
array([0, 1, 2, 3, 4])
>>> a.fill(0)
>>> a
array([0, 0, 0, 0, 0])
```

# random.randint

gives a array of integers in the defined range of the defined shape

```
>>> np.random.randint(10,55,(3,4,2))
array([[[54, 30],
        [26, 45],
        [46, 38],
        [35, 11]],

       [[20, 49],
        [42, 29],
        [11, 44],
        [26, 27]],

       [[47, 19],
        [28, 26],
        [20, 25],
        [18, 43]]])
```

# argsort

gives the position of the element in a sorted array

```
>>> import numpy as np
>>> a = np.array([1,2,3])
>>> np.argsort(a)
array([0, 1, 2])
>>> a = np.array([1,2,3,1])
>>> np.argsort(a)
array([0, 3, 1, 2])
```

# sum

```
>>> a = np.array([1,2,3])
>>> b = np.sum(a)
>>> print(b)
5
```

# append

```
>>> a = np.array([1])
>>> np.append(a, 1)
array([1, 1])
```


# argpartition(a, K)

outputs an array of indices

in the array of indices, the first K elements are the indices of the K smallest elements in a

```
>>> a = np.array([9,2,9,5,4])
>>> np.argpartition(a, 2)
array([1, 4, 3, 2, 0])
```

# unravel_index(flat_index, shape, order='F'|'C')


converts a flat index into its corresponding 2D coordinates (row, column) based on the specified array shape and order (row major or column major)

```
import numpy as np
shape = (3,3)
flat_index
```

# numpy.dot()

```
>>> a = np.random.randint(1,5,(5))
>>> b = np.random.randint(1,5,(5))
>>> c = np.dot(a,b)
>>> print(a,b,c)
[2 4 2 2 4] [4 4 2 4 2] 44
```

for 2d matrices np.dot(a,b) is actual matrix multiplication while a*b is just the multiplication of the corresponding elements

```
>>> a
array([[0, 2],
       [1, 4]])
>>> b
array([[0, 1],
       [3, 4]])
>>> np.dot(a,b)
array([[ 6,  8],
       [12, 17]])
>>> a*b
array([[ 0,  2],
       [ 3, 16]])
```

# np.linalg.det()

compute determinant

```
>>> a = np.random.randint(1,5,(2,2))
>>> a
array([[3, 2],
       [4, 3]])
>>> np.linalg.det(a)
```

# np.linalg.inv()

compute inverse of square matrix

```
>>> import numpy as np
>>> a = np.random.randint(1,5,(2,2))
>>> a
array([[3, 3],
       [2, 1]])
>>> np.linalg.inv(a)
array([[-0.33333333,  1.        ],
       [ 0.66666667, -1.        ]])
>>> np.dot(a,np.linalg.inv(a))
array([[1.00000000e+00, 2.22044605e-16],
       [1.11022302e-16, 1.00000000e+00]])
>>> np.dot(a,np.linalg.inv(a)).astype(int)
array([[1, 0],
       [0, 1]])
```

# np.newaxis

np.newaxis adds a new axis (dimension) to an array, allowing it to be broadcasted properly.

arrayexample1d[:, np.newaxis, np.newaxis] transforms arrayexample1d into a 3D array, making it compatible for element-wise multiplication.
