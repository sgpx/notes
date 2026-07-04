"""
Given A=[ 
1
2
​	
  
3
4
​	
 ] and B=[ 
2
1
​	
  
0
5
​	
 ], calculate the matrix product AB by hand, then write a 3-line NumPy script to verify it.

A 
= 
1 3
2 4

B
=
2 0
1 5

AxB 

=

(1*2 + 3*1) (1*0 + 3*5)
(2*2 + 4*1) (2*0 + 4*5)

=

2+3 15
4+4 20

=

5 15
8 20
"""

import numpy as np

a = [[1,3],[2,4]]
b = [[2,0],[1,5]]
ans = [[5, 15],[8,20]]

r = np.matmul(a,b)
print(r, ans)

print(np.all(np.equal(r, ans)))
