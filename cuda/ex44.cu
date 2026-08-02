// Write a kernel that uses __constant__ memory 

#define CONST_MEMORY_LEN_ITEMS 3
#include <cuda_runtime.h>
#include <iostream>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

__constant__ float coeffs[CONST_MEMORY_LEN_ITEMS];

void CUDA_CHECK(cudaError_t result) {
        if (result != cudaSuccess) {
                std::cout << "error" << cudaGetErrorString(result) << std::endl ;
                cudaDeviceReset();
                exit(result);
        }
}

__global__ void example_kernel(float *d_A, float *d_res, int N) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) {
        float a = d_A[i];
        d_res[i] = a * coeffs[0] + a * coeffs[1] + a * coeffs[2];
    }
}

int main() {
	float h_coeffs[CONST_MEMORY_LEN_ITEMS] = { 1.0f, 4.0f, 9.0f };
	cudaMemcpyToSymbol(coeffs, h_coeffs, sizeof(float)*CONST_MEMORY_LEN_ITEMS);
	int N = 1024, num_threads = 256;
	int num_blocks = GET_NUM_BLOCKS(N, num_threads);
	float *h_A, *h_res, *d_A, *d_res;
	h_A = (float*)malloc(N*sizeof(float));
	h_res = (float*)malloc(N*sizeof(float));
	CUDA_CHECK(cudaMalloc((void**)&d_A, N*sizeof(float)));
	CUDA_CHECK(cudaMalloc((void**)&d_res, N*sizeof(float)));
	for(int i = 0; i < N; i++){  h_A[i] = i % 5; }
	cudaMemcpy(d_A, h_A, N*sizeof(float), cudaMemcpyHostToDevice);
	example_kernel<<<num_blocks, num_threads>>>(d_A, d_res, N);
	cudaMemcpy(h_res, d_res, N*sizeof(float), cudaMemcpyDeviceToHost);
	for(int i = 0; i < N; i++){  std::cout << h_A[i] << " " << h_res[i] << std::endl ; }
	free(h_A);
	free(h_res);
	CUDA_CHECK(cudaFree(d_A));	
	CUDA_CHECK(cudaFree(d_res));	
	return 0;
}
