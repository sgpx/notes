#include <cuda_runtime.h>
#include <iostream>

int main() {
	const int N = 10000 ;
	size_t size = N * sizeof(int);
	int *d_ptr = NULL;
	int *h_ptr = NULL;

	h_ptr = (int*) malloc(size);
	std::cout << "allocating 10k.." << std::endl;
	int err = cudaMalloc(&d_ptr, size);
	if(err) {
		std::cout << "error: " << err << std::endl;
		return 1;
	}
	err = cudaMemcpy(d_ptr, h_ptr, size, cudaMemcpyHostToDevice);
	if(err) {
		std::cout << "error: " << err << std::endl;
		return 1;
	}
	std::cout << "freeing 10k.." << std::endl;
	cudaFree(d_ptr);
	free(h_ptr);

	return 0;
}
