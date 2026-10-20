/*

2D Guarded Matrix Add (#123, #124): Add two 100×150 matrices using dim3(16,16) blocks and boundary guards

*/

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

__global__ void add_matrices(int *d_A, int *d_B, int *d_C, int M, int N) {
	int col = threadIdx.x + (blockDim.x * blockIdx.x);
	int row = threadIdx.y + (blockDim.y * blockIdx.y);

	if(row < M && col < N) {
		int idx = row * N + col;
		d_C[idx] = d_A[idx] + d_B[idx];
	}
}

int main() {
	const int N = 100, M = 150;
	const int bytes = sizeof(int) * N * M;
	int *h_A, *h_B, *h_C, *d_A, *d_B, *d_C;
	h_A = (int*)malloc(bytes);
	h_B = (int*)malloc(bytes);
	h_C = (int*)malloc(bytes);
	for(int i = 0; i < N*M; i++) {
		h_A[i] = std::rand() % 100;
		h_B[i] = std::rand() % 100;
	}
	cudaError_t err = cudaMalloc((void**)&d_A, bytes);
	CUDA_CHECK(err);

	err = cudaMalloc((void**)&d_B, bytes);
	CUDA_CHECK(err);

	err = cudaMalloc((void**)&d_C, bytes);
	CUDA_CHECK(err);

	err = cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice);
	CUDA_CHECK(err);

	err = cudaMemcpy(d_B, h_B, bytes, cudaMemcpyHostToDevice);
	CUDA_CHECK(err);

	dim3 blockDim(16,16);
	dim3 gridDim(GET_NUM_BLOCKS(N, blockDim.x), GET_NUM_BLOCKS(M, blockDim.y));
	add_matrices<<<gridDim, blockDim>>>(d_A, d_B, d_C, M, N);
	
	cudaDeviceSynchronize(); 

	err = cudaMemcpy(h_C, d_C, bytes, cudaMemcpyDeviceToHost);
	CUDA_CHECK(err);

	free(h_A);
	free(h_B);
	free(h_C);
	cudaFree(d_A);
	cudaFree(d_B);
	cudaFree(d_C);

	return 0;
}
