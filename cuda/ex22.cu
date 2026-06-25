#include <cuda_runtime.h>
#include <cstdio>

int main() {
	int width = 1024;
	int height = 512;

	float *d_data;
	size_t pitch;

	cudaMallocPitch((void**)&d_data, &pitch, width * sizeof(float), height);
	printf("Allocated pitch memory: %d x %d\n" , width, height);
	printf("Pitch (in bytes):%lu\n", pitch);

	cudaFree(d_data);
}
