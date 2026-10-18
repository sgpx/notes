// Write a CUDA kernel to manually compute the element-wise exponential e^x of a 1D float array, and store the result in a new array.

#include <cuda_runtime.h>
#include <iostream>

__global__ void expkern(float *d_ptr, float *d_res, int N) {
	int tid = (blockDim.x*blockIdx.x) + threadIdx.x;
	if(tid < N) {
		d_res[tid] = __expf(d_ptr[tid]);
	}
}

int main() {
	int N = 1024;
	size_t sz = sizeof(float);
	int num_threads = 256;
	int num_blocks = (N + num_threads - 1) / num_threads;
	float *h_A, *d_A, *d_res;
	h_A = (float*)malloc(sz*N);
	cudaError_t err1 = cudaMalloc((void**)&d_A, sz*N);
	cudaError_t err2 = cudaMalloc((void**)&d_res, sz*N);
	if (err1 != cudaSuccess || err2 != cudaSuccess) {
		std::cerr << "cudaMalloc failed!" << std::endl;
		return 1;
	}
	for(int i = 0 ; i < N ; i++ ) {
		h_A[i] = (i+1) % 10;
	}
	cudaMemcpy(d_A, h_A, sz*N, cudaMemcpyHostToDevice);
	expkern<<<num_blocks, num_threads>>>(d_A, d_res, N);
	cudaDeviceSynchronize();
	cudaMemcpy(h_A, d_res, sz*N, cudaMemcpyDeviceToHost);
	for(int i = 0 ; i < N ; i++ ) {
		std::cout << i << ":" << h_A[i] << std::endl;
	}	

	free(h_A);
	cudaFree(d_A);
	cudaFree(d_res);
	return 0;
}
