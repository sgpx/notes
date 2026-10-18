/*
Implement a CUDA kernel that performs a separable 1‑D blur on a grayscale image using shared memory, then compare the runtime and quality of the blur with a naive global‑memory implementation; use NVIDIA Nsight Systems to profile both kernels and write a brief analysis of how thread‑block size and shared‑memory usage affect performance.

*/

#include <cuda_runtime.h>
#include <iostream>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

void CUDA_CHECK(cudaError_t result) {
        if (result != cudaSuccess) {
                std::cout << "error" << cudaGetErrorString(result) << std::endl ;
                cudaDeviceReset();
                exit(result);
        }
}

int main() {
	return 0;
}
