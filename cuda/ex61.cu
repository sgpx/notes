/*
2D dim3 Indexing (#124): Launch a 2×2 grid of 2×2 blocks and printf global (row, col)
*/

#include <cuda_runtime.h>
#include <cstdio>
#include <iostream>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

void CUDA_CHECK(cudaError_t result) {
        if (result != cudaSuccess) {
                std::cout << "error" << cudaGetErrorString(result) << std::endl ;
                cudaDeviceReset();
                exit(result);
        }
}

__global__ void mykernel() {
	int col = blockIdx.x * blockDim.x + threadIdx.x;
	int row = blockIdx.y * blockDim.y + threadIdx.y;
	printf("%d %d\n", row, col);
}

int main() {
	dim3 a(2,2);
	mykernel<<<a, a>>>();
	CUDA_CHECK(cudaGetLastError());
	CUDA_CHECK(cudaDeviceSynchronize());

	return 0;
}
