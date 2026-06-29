If you want to test if you've really got it, try to decompose this matrix:


$$A = \begin{bmatrix} 2 & 1 \\ 4 & 7 \end{bmatrix}$$

* **Goal:** Find $L$ and $U$ such that $A = LU$.
* **Hint:** You need to eliminate the `4` in the bottom left. What number do you multiply the first row by to turn that `4` into a `0`? That number goes into $L$.

Solution:

a = [[2,4],[1,7]]

L = l1 0
    l3 l4

U = u1 u2
    0  u4


=> 
l1*u1 l1*u2
l3*u1 l3*u2 + l4*u4 


= 

2 4
1 7


l1*u1 = 2

l1*u2 = 4

l3*u1 = 1

l3*u2 + l4*u4 = 7



(1/u1)*u2 + (l4)*u4 = 7

l4*u4 = 5

l4 and u4 can be one of {1,5}


l3*u2 = 2

l3*u1 = 1

l1*u1 = 2

l1*u2 = 4

l1 = 2, l3 = 1


L = 

2 0
1 1


U =

1 2
0 5
