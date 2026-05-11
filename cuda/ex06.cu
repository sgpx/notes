//8,__global__ kernel,Write a simple kernel that adds 1 to every element in an array and launch it,CUDA C/C++

#include <iostream>
#include <cuda_runtime.h>

void __global__ addOne(int * data, int n) {
	int idx = blockIdx.x * blockDim.x + threadIdx.x ;
	if(idx < n) {
		data[idx] += 1;
	}
}

int main() {
	int * h_ptr = NULL;
	int * d_ptr = NULL;
	size_t size = 100;
	cudaMallocHost(&h_ptr, size);
	int n = size / sizeof(int) ;

	for(int i = 0 ; i < n ; i++ ) {
		h_ptr[i] = i*2;
		std::cout << "h_ptr[" << i << "] : " << h_ptr[i] << std::endl;
	}
	std::cout << "sending to gpu" << std::endl;
	cudaMalloc(&d_ptr, size);
	cudaMemcpy(d_ptr, h_ptr, size, cudaMemcpyHostToDevice);

	int blockSize = 256;
	int gridSize = (n + blockSize - 1) / blockSize;

	addOne<<<gridSize, blockSize>>>(d_ptr,n);
	cudaDeviceSynchronize();

	cudaMemcpy(h_ptr, d_ptr, size, cudaMemcpyDeviceToHost);

	for(int i = 0 ; i < n ; i++) {
		std::cout << "h_ptr[" << i << "] : " << h_ptr[i] << std::endl;
	}
	cudaFree(d_ptr);
	cudaFreeHost(h_ptr);
	return 0;
}
