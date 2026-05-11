```cpp
#include <iostream>
#include <cuda_runtime.h>

__global__ void addOne(int* data, int n) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n) {
        data[idx] += 1;
    }
}

int main() {
    int* h_ptr = NULL;
    int* d_ptr = NULL;
    size_t size = 10 * sizeof(int);
    int n = size / sizeof(int);

    cudaMallocHost(&h_ptr, size);
    for (int i = 0; i < n; i++) {
        h_ptr[i] = i * 2;
    }

    cudaMalloc(&d_ptr, size);
    cudaMemcpy(d_ptr, h_ptr, size, cudaMemcpyHostToDevice);

    int blockSize = 256;
    int gridSize = (n + blockSize - 1) / blockSize;
    addOne<<<gridSize, blockSize>>>(d_ptr, n);

    cudaDeviceSynchronize();

    cudaMemcpy(h_ptr, d_ptr, size, cudaMemcpyDeviceToHost);

    for (int i = 0; i < n; i++) {
        std::cout << h_ptr[i] << " ";
    }
    std::cout << std::endl;

    cudaFree(d_ptr);
    cudaFreeHost(h_ptr);
    return 0;
}
```

# CUDA Kernel Launch Configuration and Execution

The block from `blockSize` definition through the `addOne<<<>>>` call sets up and executes the kernel on the GPU. Here's what each line does:

## Block Size and Grid Size Calculation

**`int blockSize = 256;`** — Sets **256 threads per block**. This is a common choice that balances occupancy and efficiency on most GPUs.

**`int gridSize = (n + blockSize - 1) / blockSize;`** — Calculates **how many blocks are needed** to cover all `n` elements. The formula `(n + blockSize - 1) / blockSize` is a ceiling division that ensures you have enough blocks. For example, if `n = 10` and `blockSize = 256`, then `gridSize = (10 + 255) / 256 = 1` block (one block can handle 10 threads). If `n = 512`, then `gridSize = (512 + 255) / 256 = 3` blocks.

## Kernel Launch

**`addOne<<<gridSize, blockSize>>>(d_ptr, n);`** — This is the actual kernel launch with the `<<<>>>` execution configuration syntax:

- **`gridSize`** (first parameter) = **number of blocks** in the grid
- **`blockSize`** (second parameter) = **number of threads per block**
- **`(d_ptr, n)`** = **function arguments** passed to the kernel

So the GPU will create `gridSize × blockSize` threads total (with some possibly being unused if `n` is not evenly divisible by `blockSize`). Each thread runs the `addOne` function independently. Inside `addOne`, the line `if (idx < n)` prevents out-of-bounds threads from accessing memory beyond the 10 elements.

---

## Synchronization

**`cudaDeviceSynchronize();`** — **Waits for all GPU operations to complete** before continuing on the CPU. Without this, the next `cudaMemcpy` might execute before the kernel finishes, giving you incorrect results.

# CUDA Execution Model: Threads, Blocks, and Streams

## Thread

**A thread is the smallest unit of execution in CUDA.** Each thread runs a copy of the kernel code independently with its own local variables and registers. Threads have a unique identifier within their block (`threadIdx.x`, `threadIdx.y`, `threadIdx.z`) that lets each thread know which piece of data to work on.

In your example, each thread executes `addOne`, calculates its own `idx`, and increments `data[idx]` by 1. With 256 threads per block, 256 copies of the kernel run in parallel.

---

## Block

**A block is a group of threads that execute together and can synchronize with each other.** Blocks have:

- A unique identifier in the grid (`blockIdx.x`, `blockIdx.y`, `blockIdx.z`)
- A configurable size (up to ~1024 threads per block on modern GPUs)
- **Shared memory** — a fast, on-chip memory visible to all threads in that block
- **Synchronization capability** — `__syncthreads()` pauses all threads in a block until everyone reaches that point

In your example, you have `gridSize` blocks, each containing 256 threads. Threads in different blocks **cannot directly communicate** or synchronize; they run independently.

---

## Stream

**A stream is a sequence of operations (kernels, memory copies) that execute in order on the GPU.** By default, all operations use stream 0 (the default stream). Streams allow you to:

- **Queue multiple operations** without blocking the CPU
- **Run operations concurrently** on different streams (if GPU resources allow)
- **Overlap computation and memory transfer** — copy data while a kernel runs on another stream

### Example with streams:
```cuda
cudaStream_t stream1, stream2;
cudaStreamCreate(&stream1);
cudaStreamCreate(&stream2);

// Queue kernel on stream1
kernel<<<grid, block, 0, stream1>>>(data1);

// Queue memory copy on stream2 (can happen while kernel runs on stream1)
cudaMemcpyAsync(data2, host_data2, size, cudaMemcpyHostToDevice, stream2);

// Wait for both to finish
cudaStreamSynchronize(stream1);
cudaStreamSynchronize(stream2);
```

---

## Quick Comparison Table

| Concept | Purpose | Scope | Communication |
|---------|---------|-------|---|
| **Thread** | Execute kernel code independently | Individual worker | Local variables, registers only |
| **Block** | Group threads for coordination | ~1–1024 threads | Shared memory, `__syncthreads()` |
| **Stream** | Order GPU operations | Multiple kernels/copies | Implicit ordering within stream |

In your code, the GPU launches `gridSize` blocks across its multiprocessors, each with 256 threads, all in the default stream. The blocks distribute the work of incrementing 10 integers in parallel.

## What is a Thread, Block, and Stream in CUDA

**CUDA organizes parallel computation hierarchically into threads, blocks, and streams**, which together form the execution model for GPU programming.

---

## Threads

**A thread is the smallest unit of execution in CUDA.** Each thread executes the same kernel code but operates on different data. Threads are extremely lightweight—GPUs can efficiently manage thousands or millions of them. Each thread has its own:

- Local registers
- Program counter
- Stack memory

Threads execute in parallel on GPU cores. When you launch a CUDA kernel, you specify how many threads to create, and each thread is assigned a unique thread ID (accessible via `threadIdx`).

---

## Blocks

**A block is a group of threads that execute together and can synchronize with each other.** Key characteristics:

- A block can contain up to **1,024 or 2,048 threads** (depending on GPU architecture)
- Threads within a block can:
  - Synchronize using `__syncthreads()` barriers
  - Cooperatively load data into shared memory
  - Communicate efficiently through shared memory
- Each block is assigned a unique block ID (accessible via `blockIdx`)
- Blocks execute independently—they cannot directly communicate or synchronize with other blocks

Blocks are the fundamental unit of work distribution. The GPU schedules blocks onto streaming multiprocessors (SMs), and all threads in a block run on the same SM.

---

## Streams

**A stream is a sequence of operations (kernel launches and memory transfers) that execute in order on the GPU.** Key characteristics:

- Operations in the same stream execute sequentially
- Operations in **different streams can overlap and execute concurrently**
- By default, there is one implicit stream (stream 0)
- You can create multiple streams to hide latency and improve GPU utilization

For example, you might use one stream for computation while another performs data transfers.

---

## How They Work Together

| Concept | Role | Size Limits | Scope |
|---------|------|-------------|-------|
| **Thread** | Smallest execution unit | N/A (millions possible) | Individual computation |
| **Block** | Group of cooperative threads | 1,024–2,048 threads | Shared memory & synchronization |
| **Stream** | Sequence of GPU operations | N/A | Asynchronous execution pipeline |

A typical kernel launch looks like:

```cuda
kernel<<<numBlocks, threadsPerBlock, sharedMemory, stream>>>(args);
```

- `numBlocks`: number of thread blocks (grid dimension)
- `threadsPerBlock`: number of threads per block (block dimension)
- `sharedMemory`: optional shared memory per block
- `stream`: which stream to execute in

**Example**: Launching 100 blocks with 256 threads each creates 25,600 threads total. These threads are grouped into 100 blocks of 256. If you launch this in two different streams, the operations can potentially overlap on the GPU.	
