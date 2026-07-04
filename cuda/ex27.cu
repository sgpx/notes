#include <cuda_runtime.h>
#include <iostream>

int main() {
	int deviceCount = 0;
	cudaGetDeviceCount(&deviceCount);
	for(int i = 0; i < deviceCount; i++) {
		cudaDeviceProp cdp;
		cudaGetDeviceProperties(&cdp, i);
		std::cout << i << std::endl;
		std::cout << "Device Name: " << cdp.name << std::endl;
		std::cout << "Device Total Memory: " << cdp.totalGlobalMem / (1024*1024) << std::endl;
	}
	return 0;
}
