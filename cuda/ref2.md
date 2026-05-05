id,topic,problem_description,language
1,nvcc,Compile a simple CUDA program that prints "Hello from GPU" using nvcc with appropriate flags,CUDA C/C++
2,cudaGetDeviceCount,Write a program that queries and prints the number of CUDA-capable GPUs available,CUDA C/C++
3,cudaSetDevice,Write a program that sets the current device to GPU 0 and verifies the selection,CUDA C/C++
4,cudaMalloc,Allocate 1MB of GPU memory and verify the allocation was successful,CUDA C/C++
5,cudaFree,Allocate 10MB of GPU memory and then free it while checking for memory errors,CUDA C/C++
6,cudaMemcpy,Copy a 1D array of 1000 integers from host to device and back to verify correctness,CUDA C/C++
7,cudaMemcpyAsync,Use cudaMemcpyAsync to transfer 10MB of data from host to device with a stream,CUDA C/C++
8,__global__ kernel,Write a simple kernel that adds 1 to every element in an array and launch it,CUDA C/C++
9,__host__ and __device__,Write a utility function that works on both host and device to compute element-wise sum,CUDA C/C++
10,Launch configuration,Launch a kernel with a 16x16 block grid to process a 256x256 matrix,CUDA C/C++
11,threadIdx and blockIdx,Write a kernel that computes a unique index for each thread using threadIdx and blockIdx,CUDA C/C++
12,__syncthreads,Write a kernel that uses shared memory and __syncthreads to compute a block-level sum reduction,CUDA C/C++
13,cudaDeviceSynchronize,Write a program that launches a kernel and uses cudaDeviceSynchronize to wait for completion before reading results,CUDA C/C++
14,Global memory,Write a kernel that reads from global memory with coalesced access patterns,CUDA C/C++
15,Shared memory,Write a kernel that uses __shared__ to cache tile data for faster computation,CUDA C/C++
16,Constant memory,Write a kernel that uses __constant__ memory to store a filter kernel for convolution,CUDA C/C++
17,Registers,Write a kernel that efficiently uses registers to compute Fibonacci numbers for each thread,CUDA C/C++
18,atomicAdd,Write a kernel where multiple threads atomically add to a shared counter and verify the final result,CUDA C/C++
19,atomicCAS,Use atomicCAS to implement a spin-lock that protects access to a shared variable,CUDA C/C++
20,cudaStream_t,Create two streams and launch kernels on both streams to overlap computation,CUDA C/C++
21,cudaStreamCreate,Create 4 CUDA streams and demonstrate async operations on each stream,CUDA C/C++
22,cudaEvent_t,Use CUDA events to measure the execution time of a kernel,CUDA C/C++
23,cudaEventElapsedTime,Measure and compare the execution time of two different matrix multiplication kernels,CUDA C/C++
24,Memory coalescing,Write two kernels that access memory in coalesced and non-coalesced patterns and compare performance,CUDA C/C++
25,__shfl_sync,Use warp shuffle operations to compute the sum of all values in a warp,CUDA C/C++
26,__warpSize,Write a kernel that uses __warpSize to optimize warp-level reductions,CUDA C/C++
27,cudaGetLastError,Write a program that intentionally causes an error and uses cudaGetLastError to detect and report it,CUDA C/C++
28,printf in kernels,Write a kernel that uses printf to debug thread indices and values,CUDA C/C++
29,Nsight Compute,Profile a simple matrix multiplication kernel using NVIDIA Nsight Compute,CUDA C/C++
30,Nsight Systems,Trace a multi-kernel CUDA program using NVIDIA Nsight Systems to visualize timeline,CUDA C/C++
31,cuBLAS gemm,Use cuBLAS to multiply two 1024x1024 matrices and compare with CPU implementation,CUDA C/C++
32,cuBLAS gemv,Use cuBLAS to multiply a 1000x1000 matrix by a 1000-element vector,CUDA C/C++
33,cuRAND,Generate 1 million random floats on the GPU using cuRAND and compute their mean,CUDA C/C++ or CuPy
34,Tensor Cores,Write a kernel using wmma API to perform matrix multiplication leveraging Tensor Cores,CUDA C/C++
35,Occupancy,Analyze a kernel and calculate theoretical occupancy given its register and shared memory usage,CUDA C/C++
36,Roofline model,Measure memory bandwidth and compute throughput of your GPU using a simple kernel,CUDA C/C++
37,Peer-to-peer,Copy data directly between GPU 0 and GPU 1 using peer-to-peer transfers,CUDA C/C++
38,Multi-GPU reduction,Write a program that reduces data across two GPUs and aggregates the result on the host,CUDA C/C++
39,Dynamic parallelism,Write a nested kernel where a parent kernel launches child kernels dynamically,CUDA C/C++
40,Cooperative groups,Use cooperative_groups API to perform a grid-level reduction,CUDA C/C++
41,Unified Memory,Use cudaMallocManaged to allocate unified memory and access it from both host and device,CUDA C/C++
42,Memory prefetch,Use cudaMemPrefetchAsync to prefetch managed memory to a GPU before kernel execution,CUDA C/C++
43,2D kernel launch,Write a kernel for 2D convolution using 2D block and grid organization,CUDA C/C++
44,Reduce operation,Implement a reduction kernel that computes the sum of all elements in an array,CUDA C/C++
45,Prefix sum,Implement an inclusive scan/prefix sum kernel for an array of integers,CUDA C/C++
46,Matrix transpose,Write a kernel that efficiently transposes a 2048x2048 matrix using shared memory,CUDA C/C++
47,Matrix multiplication,Implement matrix multiplication with optimizations like tiling and loop unrolling,CUDA C/C++
48,Histogram,Write a kernel that computes a histogram of values in an array using atomic operations,CUDA C/C++
49,Double buffering,Implement double buffering in a kernel to overlap computation and data loading,CUDA C/C++
50,__restrict__ pointers,Rewrite a memory-intensive kernel using __restrict__ pointers and measure performance difference,CUDA C/C++
