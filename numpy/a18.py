### Topic: NumPy Linear Algebra

##Exercise:## Learn about matrix multiplication and how to compute the determinant or inverse of matrices using NumPy.

##Challenge:## Write a function that takes two random square matrices of size \( n \times n \) and computes their product, determinant, and inverse (if the determinant is not zero). Print all results.

### Learning Resource:
## Familiarize yourself with `numpy.dot()`, `numpy.linalg.det()`, and `numpy.linalg.inv()` functions for matrix operations.

import numpy as np

def fxn(a, b):
        prod = np.dot(a, b)
        det_a = np.linalg.det(a)
        inv_a = np.linalg.inv(a) if det_a != 0 else None
        det_b = np.linalg.det(b)
        inv_b = np.linalg.inv(b) if det_b != 0 else None
        print(locals())    

fxn(np.random.randint(1,5,(2,2)), np.random.randint(1,5,(2,2)))
