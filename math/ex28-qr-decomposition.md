# QR decomposition

breaks any rectangular matrix into two simpler matrices Q and R

A = QR

where

Q -> m x n orthogonal matrix
R -> n x n upper triangular matrix

# properties of Q

- columns of Q form an orthonormal basis
- each column of Q has length 1
- any two columns of Q are perpendicular to each other

# properties of R

- upper triangular matrix
- all entries below diagonal are zero

# applications

- instead of solving Ax = B, you can solve Rx = Q^T . B which is numerically stable
- we can least squares problems or problems where we need to find the best fit for an equation where there are more unknowns than knowns
- QR decomposition is the standard method of computing eigenvalues 
- QR decomposition is used in systematically converting a set of vectors into orthonormal ones

