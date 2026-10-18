"""
Compute rolling statistics with vectorized operations.

Problem idea:
Given a 1D NumPy array of measurements and a window size, compute the rolling mean and rolling standard deviation without writing explicit Python loops. Use cumulative sums to make the calculations efficient, and compare the result with a simpler reference implementation.

## The Cumulative Sum Trick for Fast Window Sums

This text explains a clever algorithmic technique to **calculate rolling window sums efficiently in constant time** instead of recalculating each window from scratch.

---

## The Core Idea

The key insight is that **subtracting two cumulative sums gives you the sum of everything between them**.

If you precompute all cumulative sums once (which takes O(n) time), you can then answer "what's the sum of elements from index *i* to index *j*?" in just **O(1) time** with a single subtraction.

---

## How It Works

### Step 1: Build Cumulative Sums
The **cumulative sum** (S_k) is the total of all elements from the start up to index *k*:

[S_k = x_0 + x_1 + ... + x_k]

### Step 2: Extract Any Window
To get the sum of a window of size *w* starting at index *i*, you use:

[S_{i+w-1} - S_{i-1}]

**Why does this work?** Because:
- (S_{i+w-1}) includes everything up to the last element of your window
- (S_{i-1}) includes everything *before* your window starts
- When you subtract, all the elements before the window cancel out, leaving only your window's elements

---

## Concrete Example

Given the array **[2, 4, 6, 8, 10]**:

**Cumulative sums:** [2, 6, 12, 20, 30]
- (S_0 = 2)
- (S_1 = 2 + 4 = 6)
- (S_2 = 2 + 4 + 6 = 12)
- (S_3 = 2 + 4 + 6 + 8 = 20)
- (S_4 = 2 + 4 + 6 + 8 + 10 = 30)

For **window size 3**:
- **Window 1** [2, 4, 6]: (S_2 - S_{-1} = 12 - 0 = 12)
- **Window 2** [4, 6, 8]: (S_3 - S_0 = 20 - 2 = 18)
- **Window 3** [6, 8, 10]: (S_4 - S_1 = 30 - 6 = 24)

---

## Why This Matters

**Without cumulative sums:** Each window calculation requires summing *w* elements, giving O(n·w) time complexity for all windows.

**With cumulative sums:** One O(n) preprocessing step, then each window is O(1), giving **O(n) total time** — much faster, especially for large windows.
"""

import numpy as np
import math, random

ARRAY_LEN = 100
WINDOW_SIZE = 5

a = np.random.randint(1,10,ARRAY_LEN).astype(dtype=np.float64)

# ref code for comparison

ref = [a[i] for i in range(ARRAY_LEN)]
ref_mean = []
ref_std = []

for i in range(ARRAY_LEN):
        if i+WINDOW_SIZE > ARRAY_LEN: break
        array_slice = ref[i:i+WINDOW_SIZE]
        rolling_mean = sum(array_slice)/WINDOW_SIZE
        rolling_std = math.sqrt(sum([(val - rolling_mean)**2 for val in array_slice])/WINDOW_SIZE)
        ref_mean.append(rolling_mean)
        ref_std.append(rolling_std)
        print(i, array_slice, rolling_mean, rolling_std)

# numpy code

cumsum_raw = np.cumsum(a)
cumsum_sq = np.cumsum(a**2)
window_sums = cumsum_raw[WINDOW_SIZE-1 : ] - np.concatenate(([0], cumsum_raw[:-WINDOW_SIZE]))
window_sums_sq = cumsum_sq[WINDOW_SIZE-1 : ] - np.concatenate(([0], cumsum_sq[:-WINDOW_SIZE]))


rolling_mean = window_sums / WINDOW_SIZE
variance = (window_sums_sq / WINDOW_SIZE) - rolling_mean**2
rolling_std = np.sqrt(np.maximum(0.0, variance))
