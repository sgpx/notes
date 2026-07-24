// Write a CUDA kernel to compute the Frobenius norm of a 1024x1024 matrix using block-wise parallel sum reduction.

#include <cuda_runtime.h>
#include <iostream>
#include <cstdlib>
#include <cmath>

void CUDA_CHECK(cudaError_t result) {
        if (result != cudaSuccess) {
                std::cout << "error" << cudaGetErrorString(result) << std::endl ;
                cudaDeviceReset();
                exit(result);
        }
}

__global__ void frobenius(int *A, int M, int N, int *res) {
	
	int tid = threadIdx.x + (blockDim.x * blockIdx.x);
	for(int i = 0; i < blockDim.x ; i++) {
		int cpr = (blockDim.x + blockIdx.x) - i;
		res[i] = __sqrt(__powf(A[i], 2) + __powf(A[cpr], 2)) ;
	}

}



int main() {
	int M = 1024;
	int N = 1024;
	int num_threads = 256;
	int num_blocks = ((M*N) + num_threads - 1) / num_threads ;

	int *h_A, *d_A, *d_res, *h_res ;
	h_A = (int*)malloc(M*N*sizeof(int));
	h_res = (int*)malloc(M*N*sizeof(int));
	for(int i = 0; i < M; i++) {
		for(int j = 0; j < M; j++) {
			h_A[j + M*i] = std::rand() % 1000 ;
		}
	}
	cudaError_t err;

	err = cudaMalloc(&d_A, sizeof(int)*M*N);
	CUDA_CHECK(err);
	err = cudaMalloc(&d_res, sizeof(int)*M*N);
	CUDA_CHECK(err);

	err = cudaMemcpy(d_A, h_A, sizeof(int)*M*N, cudaMemcpyHostToDevice);
	CUDA_CHECK(err);
	frobenius<<<num_blocks, num_threads>>>(d_A, M, N, d_res);
	err = cudaMemcpy(h_res, d_res, sizeof(int)*M*N, cudaMemcpyDeviceToHost);
	CUDA_CHECK(err);

        for(int i = 0; i < M; i++) {
                for(int j = 0; j < M; j++) {
			std::cout << h_res[i][j] << " " << ;
		}
		std::cout << std::endl ;
	}

	free(h_A);
	free(h_res);
	cudaFree(d_A);
	cudaFree(d_res);
	return 0;
}
