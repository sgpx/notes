// Write a kernel that reads from global memory with coalesced access patterns

#include <cuda_runtime.h>
#include <iostream>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

void CUDA_CHECK(cudaError_t result) {
        if (result != cudaSuccess) {
                std::cout << "error" << cudaGetErrorString(result) << std::endl ;
                cudaDeviceReset();
                exit(result);
        }
}

__global__ void example_kernel(const __restrict__ int* ptr, int *res, int N) {
	int tid = threadIdx.x + (blockDim.x * blockIdx.x);
	if(tid < N) {
		res[tid] = ptr[tid]*2;
	}
}



int main() {
	int N = 100000;
	int num_threads = 256;
	int num_blocks = GET_NUM_BLOCKS(N, num_threads);
	int h_A[N], h_res[N], *d_A, *d_res;
	for(int i = 0; i < N ; i++) h_A[i] = i % 5;
	CUDA_CHECK(cudaMalloc((void**)&d_A, sizeof(int)*N));
	CUDA_CHECK(cudaMemcpy(d_A, h_A, sizeof(int)*N, cudaMemcpyHostToDevice));
	CUDA_CHECK(cudaMalloc((void**)&d_res, sizeof(int)*N));
	example_kernel<<<num_blocks, num_threads>>>(d_A, d_res, N);
	CUDA_CHECK(cudaDeviceSynchronize());
	CUDA_CHECK(cudaMemcpy(h_res, d_res, sizeof(int)*N, cudaMemcpyDeviceToHost));
	CUDA_CHECK(cudaFree(d_A));
	CUDA_CHECK(cudaFree(d_res));
	return 0;
}

/*

nvprof data

==1814== NVPROF is profiling process 1814, command: ./a.out
==1814== Profiling application: ./a.out
==1814== Profiling result:
            Type  Time(%)      Time     Calls       Avg       Min       Max  Name
 GPU activities:   47.97%  35.456us         1  35.456us  35.456us  35.456us  [CUDA memcpy HtoD]
                   43.94%  32.479us         1  32.479us  32.479us  32.479us  [CUDA memcpy DtoH]
                    8.10%  5.9840us         1  5.9840us  5.9840us  5.9840us  example_kernel(int const *, int*, int)
      API calls:   97.76%  203.55ms         2  101.78ms  17.699us  203.53ms  cudaMalloc
                    1.45%  3.0208ms       114  26.498us     126ns  1.5835ms  cuDeviceGetAttribute
                    0.60%  1.2562ms         1  1.2562ms  1.2562ms  1.2562ms  cudaLaunchKernel
                    0.16%  329.23us         2  164.62us  158.62us  170.61us  cudaMemcpy
                    0.01%  22.064us         1  22.064us  22.064us  22.064us  cuDeviceGetName
                    0.01%  15.203us         1  15.203us  15.203us  15.203us  cudaFree
                    0.00%  6.9720us         1  6.9720us  6.9720us  6.9720us  cudaDeviceSynchronize
                    0.00%  6.2690us         2  3.1340us     255ns  6.0140us  cuDeviceGet
                    0.00%  3.3910us         1  3.3910us  3.3910us  3.3910us  cuDeviceGetPCIBusId
                    0.00%  1.8220us         3     607ns     155ns  1.4330us  cuDeviceGetCount
                    0.00%     698ns         1     698ns     698ns     698ns  cuDeviceTotalMem
                    0.00%     594ns         1     594ns     594ns     594ns  cuDeviceGetUuid
                    0.00%     497ns         1     497ns     497ns     497ns  cuModuleGetLoadingMode

*/
