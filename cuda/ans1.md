# cudaMalloc

**Question:** Write a short CUDA C/C++ code snippet (≈ 20–40 lines) that demonstrates practical allocation decisions, error handling, data transfers and cleanup for a mixed CPU/GPU workflow. Use the following scenario and requirements.

Scenario (arrays of float, length N):
- constLUT (size N): initialized once on the CPU at program startup, then used read-only by many GPU kernels. It is never needed again on the host.
- input (size N): produced/changed on the CPU every iteration, consumed by the GPU kernel each iteration, and the kernel writes results back which the CPU needs for further per-iteration processing.
- tempHostOnly (size N): temporary scratch used only on the CPU (never on the GPU).

Requirements
1. For each array, choose the most appropriate allocation method (malloc, cudaMalloc, cudaMallocManaged or pinned host allocation), and briefly (1–2 sentences) justify each choice in comments.
2. Implement:
   - allocation of the three arrays,
   - initialization of constLUT on the host and transfer to device if applicable,
   - a single iteration that:
     - fills input on the host,
     - transfers it to the GPU if needed,
     - launches a kernel that reads constLUT and input and writes output into a device buffer (or managed memory) of length N (the kernel can do a simple op like output[i] = input[i] * constLUT[i]),
     - copies the output back to the host if needed,
     - uses tempHostOnly for a trivial host-only operation on the returned output.
3. Provide correct error checking for all CUDA runtime calls (store/inspect cudaError_t, print the error string) and for kernel launch use cudaGetLastError + cudaDeviceSynchronize where appropriate.
4. Free all resources properly (cudaFree / cudaFreeHost / free) even on error paths.
5. Choose and show an execution configuration for the kernel (threads per block and number of blocks) appropriate for length N.

Keep the snippet concise—focus on allocation/transfer/error-checking/cleanup. You do not need to provide a full compiled program; a self-contained function or main-like snippet is fine.

**Answer:**

#include <iostream>
#include <cuda_runtime.h>

__global__ void myKernel(const float* constLUT, const float* input, float* output, int N) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) {
        output[i] = input[i] * constLUT[i];
    }
}

bool runWorkflow(int N) {
    float* h_constLUT = nullptr;
    float* d_constLUT = nullptr;
    float* h_input = nullptr;
    float* d_input = nullptr;
    float* h_output = nullptr;
    float* d_output = nullptr;
    float* tempHostOnly = nullptr;
    
    cudaError_t err = cudaSuccess;

    // 1. constLUT: Initialized on host, used read-only on GPU
    // Justification: Allocated on host via malloc for initialization, copied to device via cudaMalloc/cudaMemcpy, 
    // and then freed from host because it is only needed on the GPU.
    h_constLUT = (float*)malloc(N * sizeof(float));
    if (!h_constLUT) goto cleanup;
    for (int i = 0; i < N; ++i) {
        h_constLUT[i] = 1.5f;
    }
    err = cudaMalloc(&d_constLUT, N * sizeof(float));
    if (err != cudaSuccess) goto cleanup;
    err = cudaMemcpy(d_constLUT, h_constLUT, N * sizeof(float), cudaMemcpyHostToDevice);
    if (err != cudaSuccess) goto cleanup;
    free(h_constLUT);
    h_constLUT = nullptr;

    // 2. input: Updated on host every iteration, consumed by GPU
    // Justification: Allocated on host as pinned memory (cudaHostAlloc) and on device (cudaMalloc). 
    // Pinned host memory is used to optimize the frequent transfers to the GPU every iteration.
    err = cudaHostAlloc(&h_input, N * sizeof(float), cudaHostAllocDefault);
    if (err != cudaSuccess) goto cleanup;
    err = cudaMalloc(&d_input, N * sizeof(float));
    if (err != cudaSuccess) goto cleanup;

    // 3. output: Written by GPU, read by CPU
    // Justification: Allocated on device via cudaMalloc and on host via standard malloc.
    // Standard pageable host memory is sufficient because output is only copied back once at the end.
    h_output = (float*)malloc(N * sizeof(float));
    if (!h_output) goto cleanup;
    err = cudaMalloc(&d_output, N * sizeof(float));
    if (err != cudaSuccess) goto cleanup;

    // 4. tempHostOnly: CPU-only temporary scratch
    // Justification: Allocated on host using standard malloc because it is only accessed by the CPU.
    tempHostOnly = (float*)malloc(N * sizeof(float));
    if (!tempHostOnly) goto cleanup;

    // Iteration loop (demonstrating single iteration)
    {
        // Produce input on CPU
        for (int i = 0; i < N; ++i) {
            h_input[i] = (float)i;
        }

        // Copy input to GPU
        err = cudaMemcpy(d_input, h_input, N * sizeof(float), cudaMemcpyHostToDevice);
        if (err != cudaSuccess) goto cleanup;

        // Launch kernel
        int threadsPerBlock = 256;
        int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
        myKernel<<<blocksPerGrid, threadsPerBlock>>>(d_constLUT, d_input, d_output, N);
        
        // Kernel launch error check & sync
        err = cudaGetLastError();
        if (err != cudaSuccess) goto cleanup;
        err = cudaDeviceSynchronize();
        if (err != cudaSuccess) goto cleanup;

        // Copy output back to CPU
        err = cudaMemcpy(h_output, d_output, N * sizeof(float), cudaMemcpyDeviceToHost);
        if (err != cudaSuccess) goto cleanup;

        // Use tempHostOnly for host-only operations on output
        float sum = 0.0f;
        for (int i = 0; i < N; ++i) {
            tempHostOnly[i] = h_output[i] * 2.0f;
            sum += tempHostOnly[i];
        }
    }

cleanup:
    // Safe resource cleanup
    if (d_constLUT) cudaFree(d_constLUT);
    if (d_input) cudaFree(d_input);
    if (d_output) cudaFree(d_output);
    if (h_input) cudaFreeHost(h_input);
    if (h_output) free(h_output);
    if (h_constLUT) free(h_constLUT);
    if (tempHostOnly) free(tempHostOnly);
    
    return (err == cudaSuccess); 
}
