// 9,__host__ and __device__,Write a utility function that works on both host and device to compute element-wise sum,CUDA C/C++

#include <cuda_runtime.h>
#include <iostream>

__host__ __device__ int xadd(int a, int b) {
	return a+b;
}

__global__ void elem_sum(int *d_A, int N, int *res) {
	int tid = blockIdx.x * blockDim.x + threadIdx.x;
	extern __shared__ int sdata[];
	int local_tid = threadIdx.x ;


	sdata[local_tid] = tid < N ? d_A[tid] : 0;
	
	for(int s = blockDim.x / 2 ; s > 0 ; s >>= 1) {
		if(local_tid < s) {
			sdata[local_tid] = xadd(sdata[local_tid], sdata[local_tid + s]);
		}
		__syncthreads();
	}
	
	if(local_tid == 0) {
		atomicAdd(res, sdata[0]);
	}
	
}


int main() {
	int N = 1024;
	size_t sz = sizeof(int);
	int *h_A, *d_A, *h_res, *d_res;
	h_A = (int*)malloc(N*sz);
	h_res = (int*)malloc(sz);
	cudaError_t err1 = cudaMalloc((void**)&d_A, N*sz);
	cudaError_t err2 = cudaMalloc((void**)&d_res, sz);
	for(int i = 0; i < N; i++){ h_A[i] = 1; }
	cudaMemcpy(d_A, h_A, N*sz, cudaMemcpyHostToDevice);
	cudaMemset((void*)d_res, 0, sz);
	int num_threads = 256;
	int num_blocks = (N + num_threads - 1) / num_threads;
	elem_sum<<<num_blocks, num_threads, num_threads * sz>>>(d_A, N, d_res);
	cudaMemcpy(h_res, d_res, 1*sz, cudaMemcpyDeviceToHost);
	std::cout << *h_res << std::endl;
	cudaFree(d_A);
	cudaFree(d_res);
	free(h_res);
	free(h_A);
	return 0;
}
