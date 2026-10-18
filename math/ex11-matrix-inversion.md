# matrix inversion

A_inv is the inverse of a matrix A such that A*A_inv = I

A = [[2,1],[5,3]]

A*A_inv = I

[[2,1],[5,3]] * [[a,b],[c,d]] = I

=>

(2a+c) (2b+d) = 1 0
(5a+3c) (5b+3d)   0 1


=>

det(A*A_inv) = det(I)

=>

10ab + 3cd + 6ad + 5bc - (10ab + 3cd + 6bc + 5ad) = 1

=>

6ad + 5bc - 6bc - 5ad = 1

=>

ad - bc = 1

2b+d = 0

b = -d/2

5a+3c = 0

a = -3c/5

-3cd/5 + cd/2 = 1

cd (1/2 - 3/5) = 1

cd * (5-6)/10 = 1

cd * -1/10 = 1

cd = -10

2a + c = 1

-6c/5 + c = 1

c = -5

d = 2

2b + d = 0
b = -1

a = -3c/5 = 15/5 = 3

therefore A_inv 

=

3 -1
-5 2


