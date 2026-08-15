/*

Write a CUDA C++ program that:

1. Accepts an integer *N* (e.g. 1024).
2. Allocates two arrays, both of length *N*:  
   - `A` (input float array)  
   - `B` (output float array)
3. Initializes all elements of `A` on the host to the value `1.5`.
4. Copies `A` from host to device.
5. **Launches a CUDA kernel that multiplies each element of `A` by 7.0, storing the result in `B`.**
6. Copies the result array `B` back to the host.
7. Prints the sum of all elements of `B` (should equal `N * 10.5`).

**Requirements:**
- Use a kernel with correct grid/block configuration.
- Remember to check for CUDA errors (at least after major operations).
- Free all device and host memory.

#### **Extensions (Optional, when done):**

- Use a `thrust::reduce` to sum the array on the device before copying to the host.
- Try timing the kernel with CUDA events.

**This exercise strengthens:**  
- Host/device memory management  
- Launch configuration (grid/block)  
- Parallel elementwise operations  
- End-to-end data movement
*/

#include <cuda_runtime.h>
#include <iostream>
#include <numeric>
#include <thrust/reduce.h>
#include <thrust/execution_policy.h>

#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

void CUDA_CHECK(cudaError_t result) {
        if (result != cudaSuccess) {
                std::cout << "error" << cudaGetErrorString(result) << std::endl ;
                cudaDeviceReset();
                exit(result);
        }
}

__global__ void multiply_by_7(float *d_A, float *d_B, int N) {
	int local = threadIdx.x;
	int tid = (blockDim.x * blockIdx.x) + local ;
	if(tid < N) {
		d_B[tid] = d_A[tid] * 7.0f;
	}

}

int main() {
	int N = 1024, num_threads = 256;
	int num_blocks = GET_NUM_BLOCKS(N, num_threads);
	float *h_A, *h_B, *d_A, *d_B;
	size_t bytes = sizeof(float) * N;
	h_A = (float*)malloc(bytes);
	h_B = (float*)malloc(bytes);
	for (int i = 0; i < N; i++) {
		h_A[i] = 1.5f;
	}
	float sum1 = thrust::reduce(thrust::host, h_A, h_A + N, 0.0f, thrust::plus<float>());
	CUDA_CHECK(cudaMalloc(&d_A, bytes));
	CUDA_CHECK(cudaMalloc(&d_B, bytes));
	CUDA_CHECK(cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice));
	cudaEvent_t start, stop;
	CUDA_CHECK(cudaEventCreate(&start));
	CUDA_CHECK(cudaEventCreate(&stop));
	CUDA_CHECK(cudaEventRecord(start, 0));
	multiply_by_7<<<num_blocks, num_threads>>>(d_A, d_B, N);
	CUDA_CHECK(cudaGetLastError());
	CUDA_CHECK(cudaEventRecord(stop, 0));
	CUDA_CHECK(cudaEventSynchronize(stop));
	float elapsedTime = 0.0f;
	CUDA_CHECK(cudaEventElapsedTime(&elapsedTime, start, stop));
	std::cout << "kernel completed in " << elapsedTime << " ms" << std::endl;
	CUDA_CHECK(cudaDeviceSynchronize());
	CUDA_CHECK(cudaMemcpy(h_B, d_B, bytes, cudaMemcpyDeviceToHost));
	float sum2 = thrust::reduce(thrust::host, h_B, h_B + N, 0.0f, thrust::plus<float>());
	std::cout << sum1 << " vs " << sum2 << std::endl;
	CUDA_CHECK(cudaEventDestroy(start));
	CUDA_CHECK(cudaEventDestroy(stop));
	free(h_A);
	free(h_B);
	CUDA_CHECK(cudaFree(d_A));
	CUDA_CHECK(cudaFree(d_B));
	return 0;
}

/*

==4409== NVPROF is profiling process 4409, command: ./a.out
kernel completed in 0.512896 ms
1536 vs 10752
==4409== Profiling application: ./a.out
==4409== Profiling result:
            Type  Time(%)      Time     Calls       Avg       Min       Max  Name
 GPU activities:   41.85%  2.4640us         1  2.4640us  2.4640us  2.4640us  multiply_by_7(float*, float*, int)
                   35.87%  2.1120us         1  2.1120us  2.1120us  2.1120us  [CUDA memcpy DtoH]
                   22.28%  1.3120us         1  1.3120us  1.3120us  1.3120us  [CUDA memcpy HtoD]
      API calls:   98.06%  174.61ms         2  87.307ms  3.3150us  174.61ms  cudaMalloc
                    1.46%  2.6075ms       114  22.873us      87ns  1.4194ms  cuDeviceGetAttribute
                    0.28%  500.37us         1  500.37us  500.37us  500.37us  cudaLaunchKernel
                    0.08%  144.30us         2  72.148us  27.483us  116.81us  cudaMemcpy
                    0.07%  118.90us         2  59.447us  10.807us  108.09us  cudaFree
                    0.01%  21.681us         2  10.840us  5.9160us  15.765us  cudaEventRecord
                    0.01%  14.055us         1  14.055us  14.055us  14.055us  cuDeviceGetName
                    0.01%  10.027us         2  5.0130us     573ns  9.4540us  cudaEventCreate
                    0.00%  7.0780us         1  7.0780us  7.0780us  7.0780us  cudaDeviceSynchronize
                    0.00%  6.2760us         2  3.1380us     199ns  6.0770us  cuDeviceGet
                    0.00%  3.7380us         1  3.7380us  3.7380us  3.7380us  cudaEventSynchronize
                    0.00%  3.7170us         2  1.8580us     662ns  3.0550us  cudaEventDestroy
                    0.00%  3.5950us         1  3.5950us  3.5950us  3.5950us  cudaEventElapsedTime
                    0.00%  2.1480us         1  2.1480us  2.1480us  2.1480us  cuDeviceGetPCIBusId
                    0.00%  1.3600us         3     453ns     111ns  1.0180us  cuDeviceGetCount
                    0.00%     583ns         1     583ns     583ns     583ns  cuDeviceTotalMem
                    0.00%     549ns         1     549ns     549ns     549ns  cuModuleGetLoadingMode
                    0.00%     414ns         1     414ns     414ns     414ns  cudaGetLastError
                    0.00%     410ns         1     410ns     410ns     410ns  cuDeviceGetUuid

*/
