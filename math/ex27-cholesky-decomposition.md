# positive symmetric definite matrix

matrix A is positive symmetric definite if

A = A^T

and 

X^T . A . X > 0

every nonzero vector X

all eigenvalues of A are strictly positive

(A-LI)V = 0

where L = { lambda_1, lambda_2 } > 0

# cholesky decomposition

cholesky decomposition breaks a positive symmetric definite matrix into the form

A = L . L^T

where L is a low triangular matrix


diagonal elements of L

L_i,i = sqrt(A_ii - sum(k=1->i-1)((L_ik)^2)

off-diagonal elements of L

for L_j,i where j > i

L_j,i = [ A_ji - sum(k=1->i-1)(L_jk)(L_ik) ]/L_ii


# applications

- symmetry: cholesky is twice as fast as standard LU decomposition because it exploits the symmetry of the matrix
- stability: it is numerically stable and does not require pivots
- applications: it is used to solve linear systems like Ax=B, do matrix inversion, generate correlated random variables in monte carlo simulations
