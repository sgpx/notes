#include <iostream>
#include <cuda_runtime.h>

int main() {
    int deviceCount = 0;
    cudaError_t err = cudaGetDeviceCount(&deviceCount);

    std::cout << err << std::endl;
	std::cout << "deviceCount: " << deviceCount << std::endl ;

	cudaDeviceProp c;
	cudaGetDeviceProperties(&c, 0);
	std::cout << c.name << std::endl ;
}
