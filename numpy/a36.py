"""
# Problem 3: Write backpropagation for a 2-layer network by hand. Given y = W2 @ (ReLU(W1 @ x + b1)) + b2, compute dL/dW1, dL/dW2.

# ref code

import torch
class SimpleNN(torch.nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = nn.Linear(4,2)
		self.relu = nn.ReLU()
		self.fc2 = nn.Linear(2,1)


	def forward(self, x):
		x = self.fc1(x)
		x = self.relu(x)
		x = self.fc2(x)
		return x

h = W1@X + b1
y = W2@relu(h) + b2

"""

import random
import math

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
	if not is_ok: raise Exception("cant be multiplied", ord1, ord2)
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



X,Y = [],[]
N = 100

for i in range(N):
	x = [float(random.randint(1,100)) for _ in range(5)]
	y = sum(x[:3]) + math.sqrt(sum(x[3:])**2) # make a relation between X and Y for the NN to approximate
	Y.append(y)
	X.append(x)

X = [X]
Y = [Y]

# xavier initialization

neuron_in = 4
neuron_out = 1
neuron_hidden = 2

xavier_limit = math.sqrt(6/(neuron_in + neuron_out))
gen_weight = lambda : random.uniform(-xavier_limit, xavier_limit)

# W1 and b1 shape must be 2,4
# W2 and b2 shape must be 1,2

W1 = [[ gen_weight() for i in range(neuron_in) ] for _ in range(neuron_hidden)]
W2 = [[ gen_weight() for i in range(neuron_hidden) ] for _ in range(neuron_out)]
b1 = [[ random.uniform(-1, 1) for i in range(neuron_hidden) ]]
b2 = [[ random.uniform(-1, 1) for i in range(neuron_out) ]]

def matsum(X, Y):
	R = [[0 for i in range(ordX[1])] for j in range(ordX[0])]	
	for nr, row in enumerate(X):
		for nc, elemX in enumerate(row):
			elemY = Y[nr][nc]
			R[nr][nc] = elemX + elemY
	return R	

def matrelu(A):
	B = [[max(0, elem) for elem in i] for i in A]
	return B	

def mat_transpose(A):
	ord = get_order(A)
	new_ord = ord[::-1]
	new_matrix = [[A[j][i] for j in range(new_ord[1])] for i in range(new_ord[0])]
	return new_matrix

def mat_hadamard_product(A, B):
	ordA = get_order(A)
	ordB = get_order(B)
	if len(ordB) != len(ordA): raise Exception("cannot multiply", ordA, ordB)
	is_allowed = all([ (i == ordB[n]) for n,i in enumerate(ordA) ])
	if not is_allowed: raise Exception("cannot multiply", ordA, ordB)
	res = [[(elem*B[nr][nc]) for nc, elem in enumerate(row)] for nr, row in enumerate(A)]
	return res			

h_orig = matsum(matmul(W1, X), b1)
h = matrelu(h_orig)
y_pred = matsum(matmul(W2, h), b2)
y_true = Y

def mseloss(y_pred, y_true):
	ord_pred = get_order(y_pred)
	loss = 0
	for nr, row in enumerate(y_pred):
		for nc, elem in enumerate(row):
			diff = y_pred[nr][nc] - y_true[nr][nc] 		
			loss += (diff ** 2)
	return loss / (ord_pred[0]*ord_pred[1])


# rate of change of loss w.r.t. output
def compute_dLdy(y_pred, y_true):
	ord_y = get_order(y_pred)
	dL_dy = [[0 for j in i] for i in y_pred]
	for nr, row in enumerate(y_pred):
		for nc, elem in enumerate(row):	
			dL_dy[nr][nc] = 2 * (y_pred[nr][nc] - y_true[nr][nc])
	return dL_dy

h_T = mat_transpose(h)
W2_T = mat_transpose(W2)

dL_dy = compute_dLdy(y_pred, y_true)
dL_dh = matmul(dL_dy, W2_T)

ord_dLdh = get_order(dL_dh)

mask = [[(1 if h_orig[nr][nc] > 0 else 0) for nc in range(len(h_orig[0]))] for nr in range(len(h_orig))]
dL_dh_pre_relu = [[dL_dh[nr][nc]*mask[nr][nc] for nc in range(ord_dLdh[1])] for nr in range(ord_dLdh[0])]

dL_dW2 = matmul(dL_dy, h_T)
dL_dW1 = matmul(dL_dh_pre_relu, mat_transpose(X))


learning_rate = 0.01

dL_db1 = dL_dy
dL_db2 = dL_dh_pre_relu

W2 -= learning_rate * dL_dW2
W1 -= learning_rate * dL_dW1
b2 -= learning_rate * dL_db2
b1 -= learning_rate * dL_db1

R1 = mat_hadamard_product(dL_dh, mask)

