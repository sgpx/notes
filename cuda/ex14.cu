#include <iostream>
#include <cuda_runtime.h>
#include <cmath>
#include <cassert>
	
__global__ void warpReduceSharedMem(int *in, int *out, int N) {
	assert(blockDim.x == 256);
	__shared__ int sdata[256];
	int tid = threadIdx.x;
	int idx = blockIdx.x * blockDim.x + threadIdx.x ;

	sdata[tid] = (idx < N) ? in[idx] : 0;

	__syncthreads();

	for(int s = blockDim.x/2; s > 0; s /= 2) {
		if(tid < s) {
			sdata[tid] += sdata[tid + s];
		}
	}
	__syncthreads();

	if(tid == 0) {
		out[blockIdx.x] = sdata[0];
	}
	__syncthreads();	
}

int main() {
	int *h_a, *h_b;
	int N = pow(10,7);
	int num_threads = 256;
	int num_blocks = (N + num_threads - 1) / num_threads;
	h_a = (int*)malloc(sizeof(int)*N);
	h_b = (int*)malloc(sizeof(int)*num_blocks);
	int *d_a, *d_b;
	cudaMalloc(&d_a, N*sizeof(int));
	cudaMalloc(&d_b, num_blocks*sizeof(int));
	for(int i = 0; i < N; i++) h_a[i] = 5*(i%2);
	cudaMemcpy(d_a, h_a, sizeof(int)*N, cudaMemcpyHostToDevice);
	warpReduceSharedMem<<<num_blocks, num_threads>>>(d_a, d_b, N);	
	cudaDeviceSynchronize();
	cudaMemcpy(h_b, d_b, sizeof(int)*num_blocks, cudaMemcpyDeviceToHost);
	unsigned long long total = 0;
	for(int i=0; i< num_blocks; i++){ 
		total += h_b[i];
		std::cout << "h_b[" << i << "] : " << h_b[i] << std::endl;
	}
	std::cout << "total: " << total << std::endl;
	free(h_a);
	cudaFree(d_a);
	cudaFree(d_b);
	return 0;
}

