"""
Given a 3×3 matrix (A=\begin{bmatrix}2&‑1&0\ -1&2&‑1\ 0&‑1&2\end{bmatrix}), compute its eigenvalues and eigenvectors analytically, then verify the results with NumPy’s numpy.linalg.eig.

# solution

A =

2 -1 0
-1 2 -1
0 -1 2

det(A-lambda*I) = 0

2-lambda -1 0
-1 2-lambda -1
0 -1 2-lambda

= (2-lambda)x{ (2-lambda)^2 - (-1)^2 } - (-1)x{(-1)x(2-lambda)}

=> (2-lambda)^3 - (2-lambda) - (2 - lambda) = 0
=> (2-lambda) { (2-lambda)^2 - 2} = 0
=> (2-lambda) (2-lambda-sqrt(2))(2-lambda+sqrt(2)) = 0

lambda = 2, 2-sqrt(2), 2+sqrt(2)


2 -1 0  a = 2a
-1 2 -1 b   2b
0 -1 2  c   2c

2a-b    = 2a
2b-a-c    2b
2c-a      2c

b = 0, a = -c

v1 = [1 0 -1]


2a-b    = (2-sqrt(2))a
2b-a-c    (2-sqrt(2))b
2c-a      (2-sqrt(2))c

b = -sqrt(2)a
-a-c = -sqrt(2)b
-a-c = -2a
a = c

v2 = [1 -sqrt(2) 1]


2a-b    = (2+sqrt(2))a
2b-a-c    (2+sqrt(2))b
2c-a      (2+sqrt(2))c

b = -sqrt(2)a
-a-c = sqrt(2)b
-a-c = -2a
a = c

-a = sqrt(2)*c

-c
"""
import numpy as np

A = np.array([ [2, -1, 0],
[-1, 2, -1],
[0, -1, 2]])

eigval, eigvec = np.linalg.eig(A)

print(eigval)
print(eigvec)
