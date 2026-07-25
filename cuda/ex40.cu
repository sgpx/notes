// 11,threadIdx and blockIdx,Write a kernel that computes a unique index for each thread using threadIdx and blockIdx,CUDA C/C++

#include <cuda_runtime.h>
#include <iostream>


void CUDA_CHECK(cudaError_t result) {
        if (result != cudaSuccess) {
                std::cout << "error: " << cudaGetErrorString(result) << std::endl ;
                cudaDeviceReset();
                exit(result);
        }
}
__global__ void uniqidx(int *ptr, int N) {
	int idx = threadIdx.x + (blockIdx.x * blockDim.x);
	if(idx < N) ptr[idx] = idx;
}


int main() {
	int N = 1024;
	int *h_res, *d_res;
	h_res = (int*)malloc(N*sizeof(int));
	cudaError_t err;
	err = cudaMalloc((void**)&d_res, sizeof(int)*N);
	CUDA_CHECK(err);
	err = cudaMemset((void*)d_res, 0, sizeof(int)*N);
	CUDA_CHECK(err);
	uniqidx<<<32,32>>>(d_res, N);
	err = cudaDeviceSynchronize();
	CUDA_CHECK(err);
	err = cudaMemcpy(h_res, d_res, sizeof(int)*N, cudaMemcpyDeviceToHost);
	CUDA_CHECK(err);
	for(int i = 0; i < N; i++) {
		std::cout << h_res[i] << std::endl;
	}
	free(h_res);
	err = cudaFree(d_res);
	CUDA_CHECK(err);
	return 0;
}
