#include <cuda_runtime.h>

__global__ void process(int *d_ptr, int N) {
	int tid = threadIdx.x + (blockDim.x * blockIdx.x);

	if(0 <= tid && tid < N) {
		d_ptr[tid] += 1; // dummy GPU operation
	}
}

void launch_kernel(int *d_ptr, int N, int num_threads_in_block) {
	int num_blocks_in_grid = (N + num_threads_in_block - 1)/num_threads_in_block;
	process<<<num_blocks_in_grid, num_threads_in_block>>>(d_ptr, N)
}

int main() {
	int N = 123456;
	int *h_ptr, *d_ptr;
	size_t sz = sizeof(int)*N;
	h_ptr = (int*)malloc(sz);
	for(int i = 0; i < N; i++) h_ptr[i] = 0;
	cudaMalloc(&d_ptr, sz);

	cudaMemcpy(d_ptr, h_ptr, sz, cudaMemcpyHostToDevice);
	launch_kernel(d_ptr, N, 256);
	cudaMemcpy(h_ptr, d_ptr, sz, cudaMemcpyDeviceToHost);
	cudaFree(d_ptr);
	for(int i = 0; i < N; i++) printf("%d : %d\n", i, h_ptr[i]);	
	free(h_ptr);
	return 0;
}
