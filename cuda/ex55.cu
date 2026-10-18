/*

Multiply two 64×64 matrices using a single thread block with __shared__ memory tiles and __syncthreads()

Add a CUDA kernel that multiplies A and B using tiled shared memory: choose a TILE_SIZE, declare two __shared__ arrays As and Bs (size TILE_SIZE x TILE_SIZE), compute each thread’s row/col in C, loop over tiles along the K dimension loading A and B tiles into shared memory, use __syncthreads() after loads, accumulate the partial sums, and finally write the result to C.
*/

#include <cuda_runtime.h>
#include <iostream>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)
#define TILE_SIZE 16

__global__ void tiled_multiply(int *A, int *B, int *C, int N) {
	__shared__ int sdata_A[TILE_SIZE*TILE_SIZE];
	__shared__ int sdata_B[TILE_SIZE*TILE_SIZE];


	int row = blockIdx.y * TILE_SIZE + threadIdx.y;
	int col = blockIdx.x * TILE_SIZE + threadIdx.x;
	if (row >= N || col >= N) return;

	int num_tiles = GET_NUM_BLOCKS(N, TILE_SIZE);

}

int main() {
	const int N = 64;
	const int bytes = sizeof(int) * N * N;

	int *h_A, *h_B, *h_C, *d_A, *d_B, *d_C;
	// 2d matrices as 1d contiguous arrays for simpler cuda processing
	h_A = malloc(bytes);
	h_B = malloc(bytes);
	h_C = malloc(bytes);

	for(int i = 0; i < N ; i++) {
		for(int j = 0; j < N; j++) {
			int curr = (i*N) + j;
			h_A[curr] = 2;
			h_B[curr] = 3;
			h_C[curr] = 0;
		}
	}

	cudaMalloc(&d_A, bytes);
	cudaMalloc(&d_B, bytes);
	cudaMalloc(&d_C, bytes);

	const int nb = GET_NUM_BLOCKS(N, TILE_SIZE);

	dim3 num_threads_per_block(TILE_SIZE, TILE_SIZE);
	dim3 num_blocks(nb, nb);


	cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice);
	cudaMemcpy(d_B, h_B, bytes, cudaMemcpyHostToDevice);
	

	tiled_multiply<<< num_blocks, num_threads_per_block >>>(d_A , d_B, d_C, N);


	cudaMemcpy(h_C, d_C, bytes, cudaMemcpyDeviceToHost);
	std::cout << h_C[0] << std::endl;

	free(h_A);
	free(h_B);
	free(h_C);

	cudaFree(d_A);
	cudaFree(d_B);
	cudaFree(d_C);

	return 0;
}
