#include <iostream>
#include <cuda_runtime.h>
#include <cassert>
	

__global void warpReduceShuffle(int *in, int *out, int N) {
	int idx = blockIdx.x * blockIdx.x + threadIdx.x;
	int val = (idx < N) ? in[idx] : 0;
	for(int offset = 16 ; offset > 0; offset >>= 1) {
		val += __shfl_xor_sync(0xffffffff, val, offset);
	}
	int lane = threadIdx.x % 32;
	int warpId = threadIdx.x / 32;
	__shared__ int warpSums[32];

	if (lane == 0) {
		warpSums[warpId] = val;
	}

	__syncthreads();

	if(warpId == 0) {
		val = (lane < blockDim.x /32) ? warpSums[lane] : 0;
		for(int offset = 16; offset > 0; offset >>= 1) {
			val += __shfl_xor_sync(0xffffffff, val, offset);
		}
		if(lane == 0) {
			out[blockIdx.x] = val;
		}
	}
}

int main() {
	int *h_a, *h_b;
	int N = 10000000;
	int num_threads = 256;
	int num_blocks = (N + num_threads - 1) / num_threads;
	h_a = (int*)malloc(sizeof(int)*N);
	h_b = (int*)malloc(sizeof(int)*num_blocks);
	int *d_a, *d_b;
	cudaMalloc(&d_a, N*sizeof(int));
	cudaMalloc(&d_b, num_blocks*sizeof(int));
	for(int i = 0; i < N; i++) h_a[i] = 5*(i%2);
	cudaMemcpy(d_a, h_a, sizeof(int)*N, cudaMemcpyHostToDevice);
  cudaEvent_t start, stop;
  cudaEventCreate(&start);
  cudaEventCreate(&stop);
  cudaEventRecord(start, 0);
	warpReduceShuffle<<<num_blocks, num_threads>>>(d_a, d_b, N);	
  cudaEventRecord(stop, 0);
  cudaEventSynchronize(stop);
  float elapsedTime = 0.0f;
  cudaEventElapsedTime(&elapsedTime, start, stop);
  std::cout << "addition happened in " << elapsedTime << " ms" << std::endl;
	cudaDeviceSynchronize();
	cudaMemcpy(h_b, d_b, sizeof(int)*num_blocks, cudaMemcpyDeviceToHost);
	unsigned long long total = 0;
	for(int i=0; i< num_blocks; i++){ 
		total += h_b[i];
		//std::cout << "h_b[" << i << "] : " << h_b[i] << std::endl;
	}
	std::cout << "total: " << total << std::endl;
	free(h_a);
	cudaFree(d_a);
	cudaFree(d_b);
	return 0;
}

