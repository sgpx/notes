#include <cuda_runtime.h>
#include <iostream>

__global__ void gpu_vector_add(float *A, float *B, float *C, int N, int a) {
  int i = blockDim.x * blockIdx.x + threadIdx.x ;

  if(i < N) {
    C[i] = B[i] + (a*A[i]);
  }
}

int main() {
  int N = 100000; 
  int scalar = 531;
  size_t size = N*sizeof(float);
  float *h_A = (float*)malloc(size);
  float *h_B = (float*)malloc(size);
  float *h_C = (float*)malloc(size);

  for(int i = 0 ; i < N ; i++) {
    h_A[i] = 1;
    h_B[i] = 2;
  }

  float *d_A, *d_B, *d_C;

  cudaMalloc(&d_A, size);
  cudaMalloc(&d_B, size);
  cudaMalloc(&d_C, size);

  cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
  cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);

  int threadsPerBlock = 256;
  int blocksPerGrid = (N + threadsPerBlock - 1)/threadsPerBlock;

  gpu_vector_add<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, N, scalar);

  cudaDeviceSynchronize();

  cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
  cudaFree(d_A);
  cudaFree(d_B);
  cudaFree(d_C);
  free(h_A);
  free(h_B);
  std::cout << "C[0] = " << h_C[0] << std::endl;
  free(h_C);
  return 0;
}
