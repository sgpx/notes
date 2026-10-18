// 12,__syncthreads,Write a kernel that uses shared memory and __syncthreads to compute a block-level sum reduction,CUDA C/C++

#include <cuda_runtime.h>
#include <iostream>

__global__ void sum_reduce(int *d_ptr, int N, int *d_res) {
	extern int __shared__ sdata[];
	int tid = threadIdx.x + (blockIdx.x * blockDim.x);
	sdata[threadIdx.x] = tid < N  ? d_ptr[tid] : 0;
	__syncthreads();
	for(int s = blockDim.x / 2 ; s > 0 ; s>>=1) {
		if(threadIdx.x < s) {
			sdata[threadIdx.x] += sdata[threadIdx.x + s];
		}
		__syncthreads();
	}
	if (threadIdx.x == 0) {
	    d_res[blockIdx.x] = sdata[0];
	}

}

int main() {
	int N = 1024;
	int num_threads = 256;
	int num_blocks = (N + num_threads - 1)/num_threads;
	int h_A[N], h_res[num_blocks];
	for(int i = 0; i < N ; i++) h_A[i] = (i % 2) ? 2 : 4;
	int *d_A, *d_res;
	cudaMalloc((void**)&d_A, sizeof(int)*N);
	cudaMalloc((void**)&d_res, sizeof(int)*N);
	cudaMemcpy(d_A, h_A, sizeof(int)*N, cudaMemcpyHostToDevice);
	sum_reduce<<<num_blocks, num_threads, num_threads*sizeof(int)>>>(d_A, N, d_res);
	cudaMemcpy(h_res, d_res, sizeof(int)*num_blocks, cudaMemcpyDeviceToHost);
	int res = 0;
	for(int i = 0; i < num_blocks; i++) {
		std::cout << h_res[i] << std::endl;
		res += h_res[i];
	}
	std::cout << "res: " << res << std::endl;
	cudaFree(d_A);
	cudaFree(d_res);
	return 0;
}
