## Chapter 3: The CUDA Execution Model: Grids, Blocks, and Threads

---

### Concept: The Hierarchical Organization of Parallelism

Unlike CPU programming where you typically think of a fixed number of threads, CUDA organizes parallel work into a **three-level hierarchy**: grids, blocks, and threads. Understanding this hierarchy is essential because it directly maps to GPU hardware, and that mapping determines whether your code runs efficiently or slowly.

**Threads** are the smallest unit. Each thread executes the same kernel code independently with its own instruction pointer and local variables. Threads are incredibly lightweight — a GPU can have hundreds of thousands of them running simultaneously.

**Blocks** are groups of threads that execute together on the same multiprocessor (SM). All threads in a block can synchronize with each other and share fast memory called shared memory. Critically, **threads in different blocks cannot reliably synchronize** — they may run in any order. A block typically contains 32 to 1024 threads, usually organized in a 1D, 2D, or 3D structure.

**Grids** are collections of blocks. A grid launches all the blocks you need to complete your entire problem. Blocks within a grid execute independently and may run in any order. The grid is also organized in 1D, 2D, or 3D.

This hierarchy exists for practical reasons: blocks map to physical hardware (each block runs on one SM), and the three-level organization lets you write code that scales from small GPUs (which might run one block at a time) to large GPUs (which might run hundreds of blocks in parallel) without changing your kernel.

---

### Toy Example: Hello from Every Thread

Here's the minimal working code that demonstrates the hierarchy:

```cuda
#include <stdio.h>
#include <cuda_runtime.h>

__global__ void helloKernel() {
    int blockId = blockIdx.x;
    int threadId = threadIdx.x;
    printf("Block %d, Thread %d\n", blockId, threadId);
}

int main() {
    // Launch 3 blocks, each with 4 threads
    helloKernel<<<3, 4>>>();
    
    // Wait for kernel to finish
    cudaDeviceSynchronize();
    
    return 0;
}
```

**What's happening:**
- `<<<3, 4>>>` means launch a grid of **3 blocks**, each containing **4 threads**
- Inside the kernel, `blockIdx.x` gives you the current block's ID (0, 1, or 2)
- `threadIdx.x` gives you the current thread's ID within its block (0, 1, 2, or 3)
- `cudaDeviceSynchronize()` waits for all blocks and threads to finish before returning

**Expected output:**
```
Block 0, Thread 0
Block 0, Thread 1
Block 0, Thread 2
Block 0, Thread 3
Block 1, Thread 0
...
```

(The actual order may vary because blocks execute independently, but you'll see output from all 12 threads total: 3 blocks × 4 threads.)

This simple example demonstrates the core concept: **you write code for a single thread, and thousands of copies of that thread run in parallel**.

---

### Measurement: Observing the Hierarchy in Action

Let's measure how the grid and block organization actually works on your GPU. Here's a program that launches kernels with different dimensions and counts how many threads execute:

```cuda
#include <stdio.h>
#include <cuda_runtime.h>

__global__ void countingKernel(int* counter) {
    // Each thread increments a counter atomically
    atomicAdd(counter, 1);
}

int main() {
    int* d_counter;
    cudaMalloc(&d_counter, sizeof(int));
    
    int h_counter = 0;
    
    // Test 1: 1 block, 32 threads
    cudaMemcpy(d_counter, &h_counter, sizeof(int), cudaMemcpyHostToDevice);
    countingKernel<<<1, 32>>>(d_counter);
    cudaMemcpy(&h_counter, d_counter, sizeof(int), cudaMemcpyDeviceToHost);
    printf("1 block × 32 threads: %d threads executed\n", h_counter);
    
    // Test 2: 4 blocks, 32 threads each
    h_counter = 0;
    cudaMemcpy(d_counter, &h_counter, sizeof(int), cudaMemcpyHostToDevice);
    countingKernel<<<4, 32>>>(d_counter);
    cudaMemcpy(&h_counter, d_counter, sizeof(int), cudaMemcpyDeviceToHost);
    printf("4 blocks × 32 threads: %d threads executed\n", h_counter);
    
    // Test 3: 100 blocks, 256 threads each
    h_counter = 0;
    cudaMemcpy(d_counter, &h_counter, sizeof(int), cudaMemcpyHostToDevice);
    countingKernel<<<100, 256>>>(d_counter);
    cudaMemcpy(&h_counter, d_counter, sizeof(int), cudaMemcpyDeviceToHost);
    printf("100 blocks × 256 threads: %d threads executed\n", h_counter);
    
    cudaFree(d_counter);
    return 0;
}
```

**Expected output:**
```
1 block × 32 threads: 32 threads executed
4 blocks × 32 threads: 128 threads executed
100 blocks × 256 threads: 25600 threads executed
```

This confirms the fundamental rule: **total threads = blocks × threads_per_block**. More importantly, you see that you control the total parallelism by choosing your grid and block dimensions.

---

### Common Mistakes

**Mistake 1: Confusing the order of grid and block dimensions in the launch syntax.**

Students often write `<<<threads, blocks>>>` instead of `<<<blocks, threads>>>`. The **first argument is always the number of blocks, the second is threads per block**. This is a frequent typo that's easy to make because the syntax isn't immediately intuitive.

```cuda
// WRONG - launches 256 blocks with 4 threads each (probably not what you want)
kernel<<<256, 4>>>();

// CORRECT - launches 4 blocks with 256 threads each
kernel<<<4, 256>>>();
```

**Mistake 2: Not understanding that blocks execute independently.**

Beginners often assume they can synchronize all threads across all blocks, or assume blocks execute in a specific order. They don't. Two blocks might run sequentially, or they might run in parallel. You cannot rely on one block finishing before another starts.

```cuda
// DON'T assume block 1 starts after block 0 finishes
// Both blocks may run simultaneously
kernel<<<2, 256>>>();
```

**Mistake 3: Launching too few blocks.**

If you have a 100-element array and launch only 1 block with 32 threads, 68 elements won't be processed. Students forget that **total threads = blocks × threads_per_block**, and if that doesn't cover your data, you need more blocks.

```cuda
// Processing 1000 elements
// If you launch <<<1, 32>>>, only 32 elements get processed!
// You need at least <<<32, 32>>> (1024 threads total)
```

**Mistake 4: Not knowing thread/block size limits.**

CUDA has hardware limits: typically **maximum 1024 threads per block** and **maximum block dimensions of 1024×1024×64**. Trying to launch `<<<1, 2048>>>` will fail silently or not launch at all. Also, the optimal thread count per block is usually **32, 64, 128, or 256** for modern hardware — multiples of the warp size (32).

```cuda
// This will fail - exceeds thread limit
kernel<<<1, 2048>>>();

// Good choice - multiple of 32 (warp size)
kernel<<<256, 256>>>();
```

**Mistake 5: Assuming blockIdx and threadIdx are always contiguous.**

If you launch <<<3, 32>>>, you get blockIdx.x ∈ {0,1,2} and threadIdx.x ∈ {0,1,...,31}. But if you launch with 2D blocks like <<<2, dim3(16,16)>>>, then threadIdx.x and threadIdx.y are both in {0,...,15}. Students often forget to account for multi-dimensional indexing.

```cuda
// 2D block: 16×16 = 256 threads
dim3 blockDim(16, 16);
kernel<<<10, blockDim>>>();

// Inside kernel, threadIdx goes from (0,0) to (15,15), not 0 to 255
```

---

### Practical Application: Parallel Matrix Transpose (Outline)

Let's see how the execution model applies to a real algorithm. Suppose you have an N×N matrix stored in row-major order and you want to transpose it.

**Sequential approach:** Loop over rows and columns, copying element [i][j] to position [j][i].

**Parallel approach:** Launch one thread per matrix element. Each thread reads its input element and writes it to the transposed position.

```cuda
#include <cuda_runtime.h>
#include <stdio.h>

__global__ void transposeKernel(float* input, float* output, int N) {
    // Each thread handles one element
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    
    // Bounds check
    if (row < N && col < N) {
        // Read from input[row][col], write to output[col][row]
        output[col * N + row] = input[row * N + col];
    }
}

int main() {
    int N = 1024;
    
    // Allocate host memory
    float* h_input = (float*)malloc(N * N * sizeof(float));
    float* h_output = (float*)malloc(N * N * sizeof(float));
    
    // Initialize input (you'd normally fill with real data)
    for (int i = 0; i < N * N; i++) {
        h_input[i] = (float)i;
    }
    
    // Allocate device memory
    float* d_input, *d_output;
    cudaMalloc(&d_input, N * N * sizeof(float));
    cudaMalloc(&d_output, N * N * sizeof(float));
    
    // Copy input to device
    cudaMemcpy(d_input, h_input, N * N * sizeof(float), cudaMemcpyHostToDevice);
    
    // Launch kernel
    // 32×32 threads per block = 1024 threads (good for hardware)
    // Need ceil(1024/32) = 32 blocks in each dimension for 1024×1024 matrix
    dim3 blockDim(32, 32);
    dim3 gridDim(N / blockDim.x, N / blockDim.y);
    transposeKernel<<<gridDim, blockDim>>>(d_input, d_output, N);
    
    // Copy result back
    cudaMemcpy(h_output, d_output, N * N * sizeof(float), cudaMemcpyDeviceToHost);
    
    // Verify (check a few elements)
    bool correct = true;
    for (int i = 0; i < 10; i++) {
        if (h_output[i * N + i] != h_input[i * N + i]) {  // Diagonal should be unchanged
            correct = false;
            break;
        }
    }
    printf("Transpose %s\n", correct ? "correct" : "incorrect");
    
    // Cleanup
    cudaFree(d_input);
    cudaFree(d_output);
    free(h_input);
    free(h_output);
    
    return 0;
}
```

**How the execution model maps to this problem:**

- Each thread handles one output element
- Threads are organized in 2D blocks (32×32) to match the 2D nature of the matrix
- We launch a 2D grid of blocks to cover the entire N×N matrix
- Within each thread, we use `blockIdx` and `threadIdx` to compute our global position in the matrix
- Each thread independently reads from input and writes to output — perfect parallel work

This is a realistic pattern: **organize blocks and threads to match your data structure**, use indexing to determine which data element(s) each thread processes, and let the GPU run thousands of threads in parallel.

---

### Summary

The CUDA execution model is a **hierarchical organization where grids contain blocks, and blocks contain threads**. This maps directly to GPU hardware: blocks run on multiprocessors, threads run on cores. By choosing grid and block dimensions appropriately, you tell the GPU how much parallelism you want and how to organize it. The key insight is that **you write code for a single thread, launch thousands of copies, and give each one an index** so it knows which data to work on.
