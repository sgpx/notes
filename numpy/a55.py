"""

## Problem: Concatenate Two 1D Arrays with `np.r_`

**Task:**
Create two NumPy 1D arrays:
- `a = np.array([1, 2, 3])`
- `b = np.array([4, 5, 6])`

Use **`np.r_`** to concatenate them row-wise into a single array, and print the result.

**Expected output:**
```
[1 2 3 4 5 6]
```

"""

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.r_[a,b])
print(np.hstack([a,b]))
