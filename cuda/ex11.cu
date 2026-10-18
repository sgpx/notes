#include <cuda_runtime.h>
#include <iostream>
#include <cmath>

__global__ void gpu_vector_ops(float *A, float *C, int N) {
  int i = blockDim.x * blockIdx.x + threadIdx.x ;

  if(i < N) {
    C[i] = A[i] > 10 ? 1 : 0 ;
  }
}

int main() {
  int N = 100000; 
  size_t size = N*sizeof(float);
  float *h_A = (float*)malloc(size);
  float *h_C = (float*)malloc(size);

  for(int i = 0 ; i < N ; i++) {
    h_A[i] = 11 * (i % 2);
  }

  float *d_A, *d_C;

  cudaMalloc(&d_A, size);
  cudaMalloc(&d_C, size);

  cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);

  int threadsPerBlock = 256;
  int blocksPerGrid = (N + threadsPerBlock - 1)/threadsPerBlock;

  gpu_vector_ops<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_C, N);

  cudaDeviceSynchronize();

  cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
  cudaFree(d_A);
  cudaFree(d_C);
  free(h_A);
  std::cout << "C[0] = " << h_C[0] << std::endl;
  std::cout << "C[1] = " << h_C[1] << std::endl;
  free(h_C);
  return 0;
}

