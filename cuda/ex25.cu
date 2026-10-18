//  Goal: Given a 2D input array $A[M][N]$, calculate the sum of all elements in the array, but structure the calculation so that it requires heavy use of shared memory within each thread block to handle the partial sums efficiently.

#include <cuda_runtime.h>
#include <cstdio>
#include <cstdlib>

__global__ void shared_memory_matrix_sum(int *d_A, int M, int N, int *d_result) {
	extern __shared__ int sdata[];

	int idx = blockIdx.x * blockDim.x + threadIdx.x ;
	int tid = threadIdx.x;

	if(idx < (M*N)) {
		int row = tid / N ;
		int col = tid % N ;
		sdata[tid] = d_A[row][col]; 
	} else {
		sdata[tid] = 0;
	}
	__syncthreads();

	for(int s = blockDim.x / 2 ; s > 0 ; s >>= 1 ) {
		if(tid < s) {
			sdata[tid] += sdata[tid + s];
		}
		__syncthreads();
	}

	if(tid == 0) {
		d_result[blockIdx.x] = sdata[0];
	}
	
}

int main() {
	int M = 3, N = 3, num_threads_in_block = 256;
	int num_blocks_in_grid = (num_threads_in_block + (M*N) - 1) / num_threads_in_block ;
	int **A, *h_result, *d_result;

	cudaMalloc(&d_result, sizeof(int) * num_blocks_in_grid);
	h_result = (int*)malloc(sizeof(int) * num_blocks_in_grid);

	A = (int**)malloc(sizeof(int*)*M);
	if(A == NULL) return 1;
	for(int i = 0; i < M; i++) {
		(A[i]) = (int*)malloc(sizeof(int)*N);
		for(int j = 0; j < N; j++) { A[i][j] = i+j; }
	}

	int **d_A;
	cudaMalloc((int**)&d_A, sizeof(int*)*M);
	for(int i = 0; i < M; i++) {
		cudaMalloc((int*)&d_A[i], sizeof(int)*N);
		cudaMemcpy(d_A[i], A[i], sizeof(int)*N, cudaMemcpyHostToDevice);
	}
	
	shared_memory_matrix_sum<<<num_blocks_in_grid, num_threads_in_block, num_threads_in_block * sizeof(int)>>>(d_A, M, N, d_result);

	for(int i = 0; i < M; i++) {
		free(A[i]);
	}
	free(A);
	cudaFree(d_A);
	return 0;
}
