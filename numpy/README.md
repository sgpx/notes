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
