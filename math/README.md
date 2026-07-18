# orthogonal vectors

two vectors, u and v are orthogonal if their dot product is 0

u = [1 -1]

v = [1 1]

u.v = (1*1) + (-1*1) = 0

# orthogonal matrix

a matrix is orthogonal if its columns or rows are orthogonal vectors and orthonormal i.e. perpendicular AND a length of 1

if the columns are orthogonal and have a value other than 1, the matrix is not orthogonal

lets say we have u = [1 -1] and v = [1 1]

u.v = 0

we will normalize the vectors so that multiplying by our matrix doesn't stretch or squeeze the space but only rotates it

if length = 1, target matrix will rotate perfectly, but if length = 2, it will stretch. reversing it will be very difficult.

therefore, we divide each vector by its magnitude

mag_u = sqrt(1**2 + (-1)**2) = sqrt(2)
mag_v = sqrt(1**2 + 1**2) = sqrt(2)

if we normalize the vectors, u' = u/mag_u = 1/sqrt(2)*u and v' = v/mag_v = 1/sqrt(2)*v

therefore our orthogonal matrix is [[1/sqrt(2) -1/sqrt(2)], [1/sqrt(2) 1/sqrt(2)]]

# LU decomposition

to solve the system AX = B 

we can break a matrix A into L and U such that

A = LU

where L is the lower triangle matrix i.e. all elements above the diagonal are zero, and U is the upper triangle matrix i.e. all elements below the diagonal are zero

=> LUX = B

now we need to solve for

Ly = B

Ux = y
	
to solve for AX = B which is computationally cheaper than solving for AX = B itself

## uses of LU decomposition

example: LU decomposition can be used to calculate the value of the ideal bridge displacement across segments using the stiffness law KD = F, where A is the stiffness matrix, X is the displacement vector and B is the force vector and we are solving for AX = B, LU decomposition makes it faster to solve these in computational simulators

# eigenvalue and eigenvectors

the eigenvector of a matrix A is a vector v to which when the matrix A is multiplied produces a lambda times scaled version of that vector that only has
 a different magnitude while possessing the same direction as before, i.e. (lambda times v) where lambda is some scalar constant

A*v = lambda*v

eigenvectors and eigenvalues only exist for square MxM matrices, they do not exist for rectangular MxN matrices

for a MxM matrix, an eigenvector dimensions are Mx1

A*v = lambda*v
=> A*v - lambda*v = 0
=> (A-lambda*I)v = 0
=> det(A-lambda*I) = 0

# SVD

we can decompose a matrix into A

A = U * sigma * V^T

let A = 

first we calculate

A^T*A  = [[3,1],[1,3]] 

A^T 

# inverse matrix

for a square matrix A, A_inv is a matrix such that

A*A_inv = I

=> A_inv*A = I

only square matrices can have inverses

the order of the inverse matrix A_inv is the same as the original matrix A

a square matrix has an inverse only if its determinant det(A) != 0


