"""
For a given grayscale image (represented as a matrix), use NumPy to perform SVD, reconstruct the image keeping only the top-k singular values, and show visually and quantitatively (Frobenius error) how compression degrades or preserves information as k varies.
"""

import numpy as np

a = np.random.rand(90000)
a = np.where(a > 0.5, 1, 0)
b = a.reshape(300, 300)

for k in range(100, 250):
	U, Sigma, V_T = np.linalg.svd(b)
	first_k_cols_of_U = U[:,:k]
	first_k_rows_of_V_T = V_T[:k, :]
	Sigma_k = np.diag(Sigma[:k])
	b_k = first_k_cols_of_U @ Sigma_k @ first_k_rows_of_V_T
	error = np.linalg.norm(b - b_k, ord='fro')
	print("k=",k, "error=",error)
