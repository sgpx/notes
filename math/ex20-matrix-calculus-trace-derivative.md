# For a n x n matrix A, prove d(Tr(AX)/dX = A^T

let A = a00 a01 a02 .. a0n
        ............... ann

X = x00 ... x0n
    ....... xnn

AX_ij = summation(k=0->n)(A_ik * X_kj)


df/dX = A^T

d(Tr(AX))/dX

=

Tr(d(AX)/X)

=

Tr(AdX)

=

Tr(A^T^T.dX)

=

Tr((df/dX)^T . dX)

=

d/dX(Tr(AX)) = A^T


