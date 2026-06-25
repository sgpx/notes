#include <cstdio>
#include <cuda_runtime.h>

__global__ void helloKernel() {
	int blockId = (int)blockIdx.x;
	int threadId = (int)threadIdx.x;

	printf("blockid %d threadid %d\n", blockId, threadId);
}

int main() {
int num_blocks = 3;
int num_threads = 4;
	helloKernel<<<num_blocks, num_threads>>>();
	cudaDeviceSynchronize();

	return 0;
}
