// 7,cudaMemcpyAsync,Use cudaMemcpyAsync to transfer 10MB of data from host to device with a stream,CUDA C/C++

#include <iostream>
#include <cuda_runtime.h>

//- `cudaStream_t stream;`
//- `cudaStreamCreate(&stream);`
//- `cudaMemcpyAsync(d_ptr, h_ptr, size, cudaMemcpyHostToDevice, stream);`

int main() {
	size_t size = 10 * 1024 * 1024;
	int * d_ptr = NULL;
	int * h_ptr = NULL;
	cudaError_t err = cudaMalloc(&d_ptr, size);
	if(err) {
		std::cout << "error" << std::endl;
		return 1;
	}
	err = cudaMallocHost(&h_ptr, size);
	if(err) {
		std::cout << "error" << std::endl;
		return 1;
	}

	for(int i = 0; i < size / sizeof(int) ; i++) {
		*(h_ptr+i) = i % 2 ? 1 : 0;
	}

	if(err) {
		std::cout << "error" << std::endl;
		return 1;
	}

	cudaStream_t stream;
	err = cudaStreamCreate(&stream);
	if(err) {
		std::cout << "error" << std::endl;
		return 1;
	}

	err = cudaMemcpyAsync(d_ptr, h_ptr, size, cudaMemcpyHostToDevice, stream);
	if(err) {
		std::cout << "error" << std::endl;
		return 1;
	}

	err = cudaStreamSynchronize(stream);
	if(err) {
		std::cout << "error" << std::endl;
		return 1;
	}

	err = cudaStreamDestroy(stream);
	if(err) {
		std::cout << "error" << std::endl;
		return 1;
	}

	err = cudaFree(d_ptr);
	if(err) {
		std::cout << "error" << std::endl;
		return 1;
	}

	err = cudaFreeHost(h_ptr);
	if(err) {
		std::cout << "error" << std::endl;
		return 1;
	}

	return 0;
}
