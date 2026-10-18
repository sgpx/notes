// Write a CUDA kernel to manually compute the element-wise exponential e^x of a 1D float array, and store the result in a new array.

#include <cuda_runtime.h>

__global__ void expsum(float *d_ptr, int N) {
	int tid = (blockDim.x*blockIdx.x) + threadIdx.x;
	if(tid < N) {
		d_ptr[tid] = __expf(d_ptr[tid]);
	}
	__syncthreads();	
}

int main() {
	int N = 1024;
	size_t sz = sizeof(float);
	int num_threads = 256;
	int num_blocks = (N + num_threads - 1) / num_threads;
	float *h_A, *d_A;
	h_A = (int*)malloc(sz*N);
	cudaError_t err = cudaMalloc((void**)&d_A, sz*N);
	for(int i = 0 ; i < N ; i++ ) {
		h_A[i] = i+1;
	}
	cudaMemcpy(d_A, h_A, sz*N, cudaMemcpyHostToDevice);
	expsum<<<num_blocks, num_threads>>>(d_A, N);
	cudaMemcpy(h_A, d_A, sz*N, cudaMemcpyDeviceToHost);
	for(int i = 0 ; i < N ; i++ ) {
		std::cout << i << ":" << h_A[i] << std::endl;
	}	

	free(h_A);
	cudaFree(d_A);
	return 0;
}
