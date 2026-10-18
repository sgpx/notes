#include <cuda_runtime.h>
#include <iostream>

int main() {
	int deviceCount = 0;

	int err = cudaGetDeviceCount(&deviceCount);
	if(err) {
		std::cout << "error" << err << std::endl;
	}

	err = cudaSetDevice(0);
	if(err) {
		std::cout << "error" << err << std::endl;
	}
	int currentDevice;
	err = cudaGetDevice(&currentDevice);
	if(err) {
		std::cout << "error" << err << std::endl;
	}
	else std::cout << "device " << currentDevice << std::endl; 

	cudaDeviceProp prop;
	cudaGetDeviceProperties(&prop, currentDevice);
	std::cout << prop.name << std::endl;

}
