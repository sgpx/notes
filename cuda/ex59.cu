/*
thrust::device_vector (#148): Allocate 8 floats set to 2.5f, modify index 0, and print without cudaMalloc.
*/

#include <cuda_runtime.h>
#include <iostream>
#include <thrust/device_vector.h>

#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

int main() {
	thrust::host_vector<float> hv(8, 2.5f);
	thrust::device_vector<float> dvec(hv);

	dvec[0] = 7.0f;
	thrust::host_vector<float> hf(dvec);
	std::cout << hf[0] << std::endl ;	

	
	return 0;
}

