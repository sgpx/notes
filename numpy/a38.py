# Problem 4: Compute SVD of a 3×2 matrix using NumPy, then verify U @ Σ @ V^T = A

import numpy as np
a = np.random.randint(size=(3,2), low=0, high=10)
U,Sigma,V_T = np.linalg.svd(a, full_matrices=False)
a2 = U @ np.diag(Sigma) @ V_T
print(a, a2)
print(np.all(np.isclose(a, a2)))
