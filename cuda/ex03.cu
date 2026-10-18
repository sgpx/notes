#include <cuda_runtime.h>
#include <iostream>

int main() {
	size_t size = 1024 * 1024 * 1024 ;

	void *d_ptr = NULL;
	std::cout << "allocating 1mb.." << std::endl;
	int err = cudaMalloc(&d_ptr, size);
	if(err) std::cout << "error" << err << std::endl;
	std::cout << "freeing 1mb.." << std::endl;
	cudaFree(d_ptr);

	return 0;
}
