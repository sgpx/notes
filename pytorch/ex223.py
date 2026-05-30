"""
Write PyTorch code to do create a non-contiguous tensor by transposing torch.arange(12).reshape(3,4), call .contiguous() to get a contiguous copy, and verify using .is_contiguous().
"""

import torch

a = torch.arange(12).reshape(3,4).T
print(a.is_contiguous()) # False

a = a.contiguous()
print(a.is_contiguous()) # True

"""
The issue here comes down to how PyTorch stores tensor data in memory and what **contiguous** means.

## What is Contiguity?

A tensor is **contiguous** when its elements are stored in memory in the exact order they appear when you iterate through the tensor. In other words, moving from one element to the next in the logical tensor layout corresponds to moving to adjacent memory locations.

## Why the First Tensor is Not Contiguous

When you do this:

```python
a = torch.arange(12).reshape(3,4).T
```

Here's what happens step by step:

1. `torch.arange(12)` creates a 1D tensor: `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`
2. `.reshape(3,4)` changes the view to a 3×4 matrix. The underlying memory still contains the same data in the same order, but PyTorch interprets it differently.
3. `.T` (transpose) flips the dimensions from 3×4 to 4×3, **but it doesn't move data around in memory**. Instead, it just changes the stride (the jump size needed to move to the next element along each dimension).

After the transpose, the tensor's logical layout doesn't match the underlying memory order, so `is_contiguous()` returns **False**.

## Why `.contiguous()` Fixes It

When you call `.contiguous()`, PyTorch creates a **new tensor** with the same logical data but physically reorganizes the memory so that elements are now stored in the order they appear logically. This new tensor has `is_contiguous() == True`.

## Why Does This Matter?

Contiguity matters for performance: some operations (like certain CUDA kernels, convolutions, or matrix multiplications) run faster or require contiguous tensors. Calling `.contiguous()` ensures compatibility and optimal performance when needed.
"""
