#include <cuda_runtime.h>
#include <iostream>

int main() {
	int c;
	cudaError_t e = cudaGetDeviceCount(&c);
	if(e != cudaSuccess) {
		std::cout << "error" << std::endl;
		std::cout << "error details: " << cudaGetErrorString(e) << std::endl;
		return 1;
	}
	std::cout << "gpu count " << c << std::endl ;
	return 0;
}
