// 10,Launch configuration,Launch a kernel with a 16x16 block grid to process a 256x256 matrix,CUDA C/C++

#include <cuda_runtime.h>
#include <iostream>

void CUDA_CHECK(cudaError_t result) {
        if (result != cudaSuccess) {
                std::cout << "error: " << cudaGetErrorString(result) << std::endl ;
                cudaDeviceReset();
                exit(result);
        }
}

__global__ void sum_kernel(int *ptr, int k, int *res) {
	int tx = threadIdx.x + blockIdx.x * blockDim.x;
	int ty = threadIdx.y + blockIdx.y * blockDim.y;
	int tid = tx + ty * (blockDim.x * gridDim.x);
	if(tid < (k*k)) atomicAdd(&res[0], ptr[tid]);
}

int main() {
	int N = 256;
	int *h_A , *h_res, *d_A , *d_res ;
	h_A = (int*)malloc(sizeof(int)*N*N);
	h_res = (int*)malloc(sizeof(int)*1);
	cudaError_t err;
	err = cudaMalloc(&d_A, sizeof(int)*N*N);
	CUDA_CHECK(err);
	err = cudaMalloc(&d_res, sizeof(int)*1);
	CUDA_CHECK(err);
	err = cudaMemset(d_res, 0, sizeof(int)*1);
	CUDA_CHECK(err);

	for(int i = 0; i < N ; i++) {
		for(int j = 0; j < N; j++) {
			h_A[N*i + j] = 1;
		}
	}
	err = cudaMemcpy(d_A, h_A, sizeof(int)*N*N, cudaMemcpyHostToDevice);
	CUDA_CHECK(err);
	dim3 grid(16, 16);
	dim3 block(16, 16);
	sum_kernel<<<grid, block>>>(d_A, N, d_res);
	err = cudaDeviceSynchronize();
	CUDA_CHECK(err);
	err = cudaMemcpy(h_res, d_res, sizeof(int)*1, cudaMemcpyDeviceToHost);
	CUDA_CHECK(err);
	std::cout << "answer: " << h_res[0] << std::endl;
	free(h_A);
	free(h_res);
	err = cudaFree(d_A);
	CUDA_CHECK(err);
	err = cudaFree(d_res);
	CUDA_CHECK(err);
	return 0;
}
