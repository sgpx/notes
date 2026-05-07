# 2,Compute matrix multiplication with nested loops,Matrix multiplication,Math Foundations,1,Linear Algebra

a = [[1,2,3],[4,5,6]]
b = [[4],[5],[1]]

def get_order(matrix):
	r = len(matrix)
	c = None
	for n,i in enumerate(matrix):
		if n == 0: c = len(i)
		else:
	return [r,c]

def can_be_multiplied(mat1, mat2):
	ord1 = get_order(mat1)
	ord2 = get_order(mat2)
	return (ord1[1] == ord2[0], ord1, ord2)


def matmul(mat1, mat2):
	is_ok , ord1 , ord2 = can_be_multiplied(mat1, mat2)
	if not is_ok: raise Exception("cant be multiplied")
	for nr,r in enumerate(mat1): pass

"""
2 2
3 3


4 5 6
5 6 7
"""

