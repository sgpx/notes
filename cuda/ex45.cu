// Write a CUDA kernel that adds two integer arrays of size `N` (e.g., `N = 1024`).  

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

__global__ void sum_kernel(int *A, int *B, int *C, int N) {
	int tid = threadIdx.x + (blockDim.x * blockIdx.x);
	if(tid < N) {
		C[tid] = A[tid] + B[tid];
	}
}

int main() {
	int N = 1024;
	int bytes = N * sizeof(int);
	int *h_A, *h_B, *h_C, *d_A, *d_B, *d_C;
	int num_threads = 256;
	int num_blocks = GET_NUM_BLOCKS(N, num_threads);
	h_A = (int*)malloc(bytes);
	h_B = (int*)malloc(bytes);
	h_C = (int*)malloc(bytes);
	for(int i = 0 ; i < N ; i++) {
		h_A[i] = i*2;
		h_B[i] = i*3;
	}
	CUDA_CHECK(cudaMalloc((void**)&d_A, bytes));
	CUDA_CHECK(cudaMalloc((void**)&d_B, bytes));
	CUDA_CHECK(cudaMalloc((void**)&d_C, bytes));
	CUDA_CHECK(cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice));
	CUDA_CHECK(cudaMemcpy(d_B, h_B, bytes, cudaMemcpyHostToDevice));
	// ---
	sum_kernel<<<num_blocks, num_threads>>>(d_A, d_B, d_C, N);
	CUDA_CHECK(cudaDeviceSynchronize());
	// ---
	CUDA_CHECK(cudaMemcpy(h_A, d_A, bytes, cudaMemcpyDeviceToHost));
	CUDA_CHECK(cudaMemcpy(h_B, d_B, bytes, cudaMemcpyDeviceToHost));
	CUDA_CHECK(cudaMemcpy(h_C, d_C, bytes, cudaMemcpyDeviceToHost));

	CUDA_CHECK(cudaFree(d_A));
	CUDA_CHECK(cudaFree(d_B));
	CUDA_CHECK(cudaFree(d_C));
	for(int i = 0 ; i < N ; i++) { 
		std::cout << h_C[i] << std::endl;
	}
	free(h_A);
	free(h_B);
	free(h_C);
	return 0;

}
