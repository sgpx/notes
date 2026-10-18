"""
### ✅ **Problem: Weighted Row Sum with Broadcasting**

**Goal**:  
Create a 3×4 NumPy array of integers from 1 to 12 (in row-major order), then multiply each **column** by a corresponding weight from a 1D array `[2, 0.5, 3, 1]`, and finally compute the **sum of each row** after weighting.

**Steps**:
1. Create a 3×4 array with numbers 1 through 12, filled row-wise.
2. Define a 1D weight array: `[2, 0.5, 3, 1]`.
3. Use **broadcasting** to multiply each column of the 3×4 array by the corresponding weight.
4. Compute the **sum of each row** in the resulting weighted array.
5. Print:
   - The original 3×4 array
   - The weight array
   - The weighted array (after broadcasting multiplication)
   - The row sums (as a 1D array)

"""

import numpy as np

a = np.arange(1,12+1).reshape(3,4)
print(a)
b = np.array([2, 0.5, 3, 1])

c = a * b
print(c)
