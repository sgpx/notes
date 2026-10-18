/*

CUDA (Index Mapping): Write an exact 3-line CUDA C++ snippet that calculates a thread's unique global 1D index from a 1D grid layout, checks if that index is within a data boundary N, and if valid, multiplies the element in global array data at that index by 2.0f.

*/

#include <cuda_runtime.h>
#include <iostream>

__global__ void mul_1d(float *A, int N) {
	const int i = threadIdx.x + blockDim.x * blockIdx.x;
	if(i < N) A[i] *= 2.0f;
} 

int main() {
	int N = 10000;
	int num_threads_per_block = 256;
	int num_blocks_per_grid = (N + num_threads_per_block - 1)/num_threads_per_block;

	float *h_A = (float*)malloc(sizeof(float)*N);
	float *d_A;
	cudaMalloc((void**)&d_A, sizeof(float)*N);
	for(int i = 0; i < N; i++) { h_A[i] = i % 5; } 

	cudaMemcpy(d_A, h_A, sizeof(float)*N, cudaMemcpyHostToDevice);
	mul_1d<<<num_blocks_per_grid, num_threads_per_block>>>(d_A, N);
	cudaMemcpy(h_A, d_A, sizeof(float)*N, cudaMemcpyDeviceToHost);

	for(int i = 0; i < N; i++) {
		std::cout << h_A[i] << std::endl;
	}
	cudaFree(d_A);
	free(h_A);
	return 0;
}
