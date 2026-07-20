// Problem: Compute the sigmoid of a float vector and compare every result against a CPU implementation
/*

y = sigmoid(x) = 1/(1+e^-x)

*/

#include <cuda_runtime.h>
#include <iostream>
#include <cstdlib>
#include <cmath>



__device__ float cuda_sigmoid(float x) {
	return __fdividef(1.0f, 1.0f + __expf(-x));
}

__global__ void sigkern(float *d_A, float *d_res, int N) {
	int tid = threadIdx.x + (blockIdx.x * blockDim.x);
	if(tid < N) {
		d_res[tid] = cuda_sigmoid(d_A[tid]);
	}
}

float sigmoid(float x) {
	return 1.0f/(1.0f + std::exp(-x));
}

char * is_close(float x, float y) {
	return (std::abs(x-y) < 1e-4) ? "true" : "false";
}

int main() {
	int N = 1024; 
	size_t sz = sizeof(float);
	int num_threads = 256;
	int num_blocks = (N + num_threads - 1 ) / num_threads;

	float *h_A, *d_A, *h_cpu_res, *h_gpu_res, *d_res ;
	h_A = (float*)malloc(sz*N);
	h_cpu_res = (float*)malloc(sz*N);
	h_gpu_res = (float*)malloc(sz*N);
	cudaMalloc((void**)&d_A, sz*N);
	cudaMalloc((void**)&d_res, sz*N);
	for(int i = 0; i < N; i++) {
		h_A[i] = -100.0f + (200.0f * ((float)rand() / RAND_MAX));
		h_cpu_res[i] = sigmoid(h_A[i]);
	}
	cudaMemcpy(d_A, h_A, sz*N, cudaMemcpyHostToDevice);
	sigkern<<<num_blocks, num_threads>>>(d_A, d_res, N);
	cudaDeviceSynchronize();
	cudaMemcpy(h_gpu_res, d_res, sz*N, cudaMemcpyDeviceToHost);
	for(int i = 0 ; i < N ; i++) {
		std::cout << i << h_A[i] << h_cpu_res[i] << h_gpu_res[i] << is_close(h_cpu_res[i], h_gpu_res[i]) << std::endl ;
	}
	cudaFree(d_A);
	cudaFree(d_res);
	free(h_A);
	free(h_cpu_res);
	free(h_gpu_res);
	return 0;
}
