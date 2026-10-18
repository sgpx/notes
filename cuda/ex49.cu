/*
Implement a CUDA kernel that computes the sum of all elements in a 1D integer array using a block-wise reduction with shared memory, then launches it on a 1024×1024 array and prints the final sum.
*/

#include <cuda_runtime.h>
#include <iostream>
#include <random>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)


void CUDA_CHECK(cudaError_t result) {
        if (result != cudaSuccess) {
                std::cout << "error" << cudaGetErrorString(result) << std::endl ;
                cudaDeviceReset();
                exit(result);
        }
}

__global__ void sum_kernel(int *ptr, int *res, int arraysize) {
	int local = threadIdx.x;
	int tid = local + (blockDim.x * blockIdx.x);

	extern __shared__ int sdata[];
	sdata[local] = (tid < arraysize) ? ptr[tid] : 0;

	for(int s = blockDim.x / 2 ; s > 0 ; s >>= 1) {
		if(local < s) {
			sdata[local] += sdata[local + s];
		}
		__syncthreads();
	}

	if(local == 0) {
		atomicAdd(res, sdata[0]);
	}
}

int main() {
	int N = 1024;
	int num_threads = 256;
	int num_blocks = GET_NUM_BLOCKS(N*N, num_threads);
	int shared_memory_size = num_threads*sizeof(int);
	int bytes = N * N * sizeof(int);
	int *h_A, *h_res, *d_A, *d_res;
	h_A = (int*)malloc(bytes);
	h_res = (int*)malloc(sizeof(int));
	CUDA_CHECK(cudaMalloc((void**)&d_A, bytes));
	CUDA_CHECK(cudaMalloc((void**)&d_res, sizeof(int)));
	for(int i = 0; i < N*N; i++) {
		h_A[i] = ((int)std::rand()) % 100;
	}
	CUDA_CHECK(cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice));
	CUDA_CHECK(cudaMemset(d_res, 0, sizeof(int)));

	sum_kernel<<<num_blocks, num_threads, shared_memory_size>>>(d_A, d_res, N*N);
	CUDA_CHECK(cudaDeviceSynchronize());
	CUDA_CHECK(cudaMemcpy(h_res, d_res, sizeof(int), cudaMemcpyDeviceToHost));
	std::cout << "the sum is " << *h_res << std::endl;
	free(h_A);
	free(h_res);
	CUDA_CHECK(cudaFree(d_A));
	CUDA_CHECK(cudaFree(d_res));
		
	return 0;
}

/*

==1312== NVPROF is profiling process 1312, command: ./a.out
the sum is 51076832
==1312== Profiling application: ./a.out
==1312== Profiling result:
            Type  Time(%)      Time     Calls       Avg       Min       Max  Name
 GPU activities:   89.05%  803.95us         1  803.95us  803.95us  803.95us  [CUDA memcpy HtoD]
                   10.64%  96.094us         1  96.094us  96.094us  96.094us  sum_kernel(int*, int*, int)
                    0.23%  2.1110us         1  2.1110us  2.1110us  2.1110us  [CUDA memcpy DtoH]
                    0.07%     672ns         1     672ns     672ns     672ns  [CUDA memset]
      API calls:   66.18%  223.80ms         2  111.90ms  102.90us  223.70ms  cudaMalloc
                   32.39%  109.53ms         1  109.53ms  109.53ms  109.53ms  cudaLaunchKernel
                    0.75%  2.5248ms       114  22.147us     122ns  1.4384ms  cuDeviceGetAttribute
                    0.52%  1.7434ms         2  871.71us  62.132us  1.6813ms  cudaMemcpy
                    0.13%  430.06us         2  215.03us  207.60us  222.47us  cudaFree
                    0.03%  90.772us         1  90.772us  90.772us  90.772us  cudaDeviceSynchronize
                    0.01%  18.179us         1  18.179us  18.179us  18.179us  cudaMemset
                    0.00%  14.030us         1  14.030us  14.030us  14.030us  cuDeviceGetName
                    0.00%  5.4130us         2  2.7060us     256ns  5.1570us  cuDeviceGet
                    0.00%  2.2300us         1  2.2300us  2.2300us  2.2300us  cuDeviceGetPCIBusId
                    0.00%  1.2630us         3     421ns     197ns     867ns  cuDeviceGetCount
                    0.00%  1.0780us         1  1.0780us  1.0780us  1.0780us  cuDeviceTotalMem
                    0.00%     533ns         1     533ns     533ns     533ns  cuDeviceGetUuid
                    0.00%     274ns         1     274ns     274ns     274ns  cuModuleGetLoadingMode

*/
