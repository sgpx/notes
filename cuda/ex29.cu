/*

Write an exact 4-line CUDA C++ kernel snippet (just the inside of a __global__ function) that reads an input array from global memory into a block-allocated __shared__ array of size 256 using the local thread ID, synchronizes the block threads to ensure memory consistency, reverses the sequence within that block, and writes it back to global memory.

*/

#include <cuda_runtime.h>
#include <cstdio>

__global__ void shared_mem_reverse(int *A, int N) {
        extern __shared__ int sdata[];
        printf("tidx %d bidx %d%c", threadIdx.x, blockIdx.x, 10);
	int idx = blockIdx.x * blockDim.x + threadIdx.x;
	if (idx < N) sdata[threadIdx.x] = A[idx];
	__syncthreads();
	if (idx < N) A[idx] = sdata[blockDim.x - 1 - threadIdx.x];
}

int main() {
        int N = 256;
        int num_threads_in_block = 256;
        int num_blocks_in_grid = (N+num_threads_in_block-1)/num_threads_in_block;

        int *h_A, *d_A;
        h_A = (int*)malloc(sizeof(int)*N);
        for(int i = 0; i < N; i++) { h_A[i] = 2*i; }

        cudaMalloc((void**)&d_A, sizeof(int)*N);
        cudaMemcpy(d_A, h_A, sizeof(int)*N, cudaMemcpyHostToDevice);
	size_t shared_mem_size = sizeof(int)*N;
        shared_mem_reverse<<<num_blocks_in_grid, num_threads_in_block, shared_mem_size>>>(d_A, N);

        cudaMemcpy(h_A, d_A, sizeof(int)*N, cudaMemcpyDeviceToHost);

        cudaFree(d_A);
        for(int i = 0; i < N ; i++) {
          printf("%d ", h_A[i]);
        }
        free(h_A);
        return 0;
}
