#include <cstdio>
#include <cuda_runtime.h>

__global__ void add_one(int *d_a) {
	int blockId = blockIdx.x;
	int threadId = threadIdx.x;

	printf("blockId %d threadId %d pre-add val %d\n", blockId, threadId, *d_a);
	atomicAdd(d_a, 1);
	printf("blockId %d threadId %d post-add val %d\n", blockId, threadId, *d_a);
}

int main() {
	int *h_a, *d_a;
	int N = 1, num_blocks = 2, num_threads = 256;
	h_a = (int*)malloc(N*sizeof(int));
	*h_a = 0;
	cudaMalloc(&d_a, N*sizeof(int));
	cudaMemcpy(d_a, h_a, N*sizeof(int), cudaMemcpyHostToDevice);
	add_one<<<num_blocks, num_threads>>>(d_a);
	cudaDeviceSynchronize();
	cudaMemcpy(h_a, d_a, N*sizeof(int), cudaMemcpyDeviceToHost);
	cudaFree(d_a);
	printf("final val %d\n", *h_a);
	free(h_a);
	return 0;
}
