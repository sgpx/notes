// pass an invalid device ID and see what happens

include <cuda_runtime.h>
include <iostream>

int main() {
	int deviceCount = 0;
	cudaError_t err = cudaGetDeviceCount(&deviceCount);
	std::cout << deviceCount << std::endl ;
	err = cudaSetDevice(999);
	std::cout << err << std::endl ;
	const char *estr = cudaGetErrorString(err);
	std::cout << estr << std::endl ;
	return 0;
}

