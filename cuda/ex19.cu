// check
// 24,cudaMalloc,Allocate 1GB of GPU memory and verify the allocation was successful,CUDA C++

#include <cuda_runtime.h>
#include <iostream>

int main() {
	unsigned long long bytes = 1024 * 1024 * 1024 * 1ULL;
	size_t N = bytes / sizeof(int);
	int *h_a;
	h_a = (int*)malloc(bytes);
	if(!h_a) std::cout << "host malloc failed" << std::endl;
	else std::cout << "host malloc success" << std::endl;
	for(size_t i = 0 ; i < N ; i++) {
		h_a[i] = i % 10;
	}
	int *d_a;
	cudaError_t c = cudaMalloc((void**)&d_a, bytes);
	if(c) {
		std::cout << "cuda malloc failed" << std::endl;
	}
	else {
		cudaError_t c2 = cudaMemcpy(d_a, h_a, bytes, cudaMemcpyHostToDevice);
		if(c2) std::cout << "cuda memcpy failed" << std::endl;
    else std::cout << "cuda memcpy success" << std::endl;
	}
	cudaError_t c3 = cudaFree(d_a);
	if(c3) std::cout << "cuda free failed" << std::endl;
  else std::cout << "cuda free succeess" << std::endl;
	free(h_a);
	return 0;
}
