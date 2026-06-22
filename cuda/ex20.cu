// Allocate memory for an array of 1000 floats and check for null pointer

#include <cuda_runtime.h>
#include <iostream>
#include <cstdlib>

int main() {
	int N = 1000;
	float *h_a;
	h_a = (float*)malloc(N*sizeof(float));
	if(h_a == NULL) { std::cout << "nullptr exception" << std::endl ; return 1 ; }

	for(float i = 0; i < N; i++){ h_a[i] = i; }
	float *d_a;
	cudaError_t c = cudaMalloc(&d_a, sizeof(float)*N);
	if(c != cudaSuccess) { std::cout << "error" << std::endl; }
	else if(d_a == NULL) { std::cout << "nullptr exception" << std::endl ; return 1; }
	cudaMemcpy(d_a, h_a, N*sizeof(float), cudaMemcpyHostToDevice);
	cudaFree(d_a);
	free(h_a);
	return 0;
}
