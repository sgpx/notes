// Write a single CUDA kernel that multiplies a 1024‑element vector by a scalar using a grid‑stride loop.

#include <cuda_runtime.h>
#include <iostream>


__global__ void scale_kernel(int *x, int N, int a) {
	for(int i = blockIdx.x * blockDim.x + threadIdx.x ; i < N ; i += gridDim.x * blockDim.x) {
		x[i] *= a;		
	}
}

int main() {
	int N = 1024;
	size_t sz = sizeof(int);
	int scalar = 55;
	
	int * h_A = (int*)malloc(sz*N);
	for(int i = 0 ; i < N ; i++) {
		h_A[i] = (5*(i+1)) % 25;
	}
	int * d_A;
	cudaMalloc((void**)&d_A, sz*N);

	cudaMemcpy(d_A, h_A, N*sz, cudaMemcpyHostToDevice);
	int num_threads = 256;
	int num_blocks = (N + num_threads - 1) / num_threads;
	scale_kernel<<<num_blocks, num_threads>>>(d_A, N, scalar);
	cudaMemcpy(h_A, d_A, N*sz, cudaMemcpyDeviceToHost);
	for(int i = 0 ; i < N ; i++) {
		std::cout << h_A[i] << std::endl;
	}	
	free(h_A);
	cudaFree(d_A);
	return 0;
} 
