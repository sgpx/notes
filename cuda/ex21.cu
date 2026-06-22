include <cuda_runtime.h>
#include <iostream>
using namespace std;

__global__ void dostuff(int * d_a, int N) {
	extern __shared__ int sdata;
	int idx = threadIdx.x + (blockIdx.x * blockDim.x);
	if(idx < N) {
		sdata[threadIdx.x] = d_a[idx];
	}
	else {
		sdata[threadIdx.x] = 0;
	}
	printf("Compilation test 1 %d %d", threadIdx.x, blockIdx.x);
	int ct = (threadIdx.x + (blockIdx.x * 256)) % N;
	printf("%d", d_a[ct]);
}

int main() {
	int N = 50000;
	int *h_a = (int*)malloc(N*sizeof(int));
	int *d_a;
	cudaMalloc(&d_a, sizeof(int)*N);
	for(int i = 0; i < N ; i++) h_a[i] = i % 10;
	cudaMemcpy(d_a, h_a, N*sizeof(int), cudaMemcpyHostToDevice);
	int num_blocks = (N + threads_per_block - 1) / threads_per_block;
	dostuff<<<num_blocks,256>>>(d_a, N);
	free(h_a);
	cudaFree(d_a);
	return 0;
}
