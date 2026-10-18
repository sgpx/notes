# Problem 2: Implement matrix multiplication from scratch (3 nested loops). Multiply [[1,2],[3,4]] × [[5,6],[7,8]] without @ or .dot().

"""
2 2
3 3


4 5 6
5 6 7
"""


import numpy as np

a = [[1,2,3],[4,5,6]]
b = [[4],[5],[1]]

a = [[1,2],[3,4]]
b = [[5,6],[7,8]]

def get_order(matrix):
	r = len(matrix)
	c = None
	for n,i in enumerate(matrix):
		if n == 0: c = len(i)
	return [r,c]

def can_be_multiplied(mat1, mat2):
	ord1 = get_order(mat1)
	ord2 = get_order(mat2)
	return (ord1[1] == ord2[0], ord1, ord2)

def get_cols(x, ord_x):
	rv = []
	r,c = ord_x
	for i in range(c):
		rv.append([row[i] for row in x])
	return rv

def matmul(mat1, mat2):
	is_ok , ord1 , ord2 = can_be_multiplied(mat1, mat2)
	if not is_ok: raise Exception("cant be multiplied")
	ord_prod = [ord1[0], ord2[1]]
	prod = []
	for i in range(ord_prod[0]):
		rv = []
		for j in range(ord_prod[1]):
			rv.append(0)
		prod.append(rv)

	mat2_cols = get_cols(mat2, ord2)

	for nr,row in enumerate(mat1):
		for nc,col in enumerate(mat2_cols): 
			elem = 0
			for f1,f2 in zip(row, col):
				elem += (f1 * f2)
			prod[nr][nc] = elem
	return prod

res = np.array(matmul(a,b))
chk = np.matmul(np.array(a), np.array(b))

print(res)
print(chk)

assert (np.allclose(res, chk))
