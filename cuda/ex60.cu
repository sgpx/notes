/*
Create a stream, launch a 1-block empty kernel on it, synchronize, and destroy.
*/

#include <cuda_runtime.h>
#include <iostream>

void CUDA_CHECK(cudaError_t result) {
        if (result != cudaSuccess) {
                std::cout << "error" << cudaGetErrorString(result) << std::endl ;
                cudaDeviceReset();
                exit(result);
        }
}
__global__ void emptyKernel() {
}

int main() {
	cudaError_t err;
	cudaStream stream;
	err = cudaStreamCreate(&stream);
	CUDA_CHECK(err);

	emptyKernel<<<1,1,0, stream>>>();
	err = cudaStreamSynchronize(stream);
	CUDA_CHECK(err);

	err = cudaStreamDestroy(stream);		
	CUDA_CHECK(err);

	return 0;
}

