// SGEMM example with cuBLAS

#include <cuda_runtime.h>
#include <cublas_v2.h>
#include <iostream>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

void CUDA_CHECK(cudaError_t result) {
    if (result != cudaSuccess){  std::cout << "error: " << result << std::endl ; exit(result); }
}

void CUBLAS_CHECK(cublasStatus_t result) {
    if (result != CUBLAS_STATUS_SUCCESS) exit(result);
}

int main() {

int device_count = 0;
cudaGetDeviceCount(&device_count);
std::cout << "Device count: " << device_count << std::endl;

int current_device = -1;
cudaGetDevice(&current_device);
std::cout << "Current device: " << current_device << std::endl;

cudaSetDevice(0);  // explicitly set device 0
std::cout << "Set device to 0" << std::endl;

	float h_A[] = {1,2,3,4};
	float h_B[] = {4,5,6,7};
	float h_C[4];

	float *d_A, *d_B, *d_C;
	std::cout << "t1" << std::endl;
	cudaError_t err = cudaMalloc(&d_A, sizeof(h_A));
	CUDA_CHECK(err);
	std::cout << "t2" << std::endl;

	CUDA_CHECK(cudaMalloc(&d_B, sizeof(h_B)));
	std::cout << "t3" << std::endl;
	CUDA_CHECK(cudaMalloc(&d_C, sizeof(h_C)));

	CUDA_CHECK(cudaMemcpy(d_A, h_A, sizeof(h_A), cudaMemcpyHostToDevice));
	CUDA_CHECK(cudaMemcpy(d_B, h_B, sizeof(h_B), cudaMemcpyHostToDevice));

	cublasHandle_t handle;

	CUBLAS_CHECK(cublasCreate(&handle));

	const float alpha = 1.0f;
	const float beta = 0.0f;

	int m = 2, n = 2, k = 2;

	int leading_dim_A = 2, leading_dim_B = 2, leading_dim_C = 2;

	CUBLAS_CHECK(cublasSgemm(handle, CUBLAS_OP_N, CUBLAS_OP_N, m, n, k, &alpha, d_A, leading_dim_A, d_B, leading_dim_B, &beta, d_C, leading_dim_C));
	CUDA_CHECK(cudaMemcpy(h_C, d_C, sizeof(h_C), cudaMemcpyDeviceToHost));

	for(int i = 0; i < 2; i++) {
		for(int j = 0; j < 2; j++) {
			std::cout << i << " " << j << " " << h_C[i + j*2] << std::endl;
		}
	}

	CUBLAS_CHECK(cublasDestroy(handle));
	CUDA_CHECK(cudaFree(d_A));
	CUDA_CHECK(cudaFree(d_B));
	CUDA_CHECK(cudaFree(d_C));
	return 0;
}
