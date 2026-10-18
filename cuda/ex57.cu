/*

Thread boundary checking with a 1D saxpy kernel (N=1000 across 4 blocks of 256 threads

Given two input vectors A and B of size N and a constant alpha, compute the output vector C such that:

    C[i] = alpha*A[i] + B[i] for all i in [0, N-1]

*/

#include <cuda_runtime.h>
#include <iostream>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

__global__ void sum_kern(int *alpha, int *A, int *B, int *C, int N) {
	int i = threadIdx.x + (blockIdx.x * blockDim.x);
	if(i < N) { C[i] = (*alpha)*A[i] + B[i]; }
}

int main() {
	int N = 1000;

	const int bytes = sizeof(int) * N;
	const int num_blocks = 4;

	int *h_A, *h_B, *h_C, *d_A, *d_B, *d_C, *h_alpha, *d_alpha;

	h_alpha = (int*)malloc(sizeof(int));
	*h_alpha = std::rand() % 100;

	h_A = (int*)malloc(bytes);
	h_B = (int*)malloc(bytes);
	h_C = (int*)malloc(bytes);
	for(int i = 0; i < N ; i++ ) {
		h_A[i] = (int)std::rand() % 100;
		h_B[i] = (int)std::rand() % 100;
	} 
	cudaMalloc((void**)&d_alpha, sizeof(int));
	cudaMalloc((void**)&d_A, bytes);
	cudaMalloc((void**)&d_B, bytes);
	cudaMalloc((void**)&d_C, bytes);
	cudaMemcpy(d_alpha, h_alpha, sizeof(int), cudaMemcpyHostToDevice);
	cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice);
	cudaMemcpy(d_B, h_B, bytes, cudaMemcpyHostToDevice); 
	sum_kern<<<num_blocks, 256>>>(d_alpha, d_A, d_B, d_C, N);
	cudaMemcpy(h_C, d_C, bytes, cudaMemcpyDeviceToHost);
	for(int i = 0; i < N; i++) { std::cout << *h_alpha << "*" << h_A[i] << "+" << h_B[i] << "=" << h_C[i] << std::endl ; }
	cudaFree(d_A);
	cudaFree(d_B);
	cudaFree(d_C);
	cudaFree(d_alpha);
	free(h_A);
	free(h_B);
	free(h_C);
	free(h_alpha);

	return 0;
}

