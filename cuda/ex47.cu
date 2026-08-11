/*
Compute the dot product of two vectors using shared memory reduction.
*/

#include <cuda_runtime.h>
#include <iostream>
#include <random>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

void CUDA_CHECK(cudaError_t result) {
    if (result != cudaSuccess) {
        std::cout << "error" << cudaGetErrorString(result) << std::endl;
        cudaDeviceReset();
        exit(result);
    }
}

__global__ void dot_product(int *d_A, int *d_B, int *d_C, int N) {
    int tid = threadIdx.x + (blockIdx.x * blockDim.x);
    int local = threadIdx.x;
    extern __shared__ int sdata[];
    int prod = 0;
    if (tid < N) {
        prod = d_A[tid] * d_B[tid];
    }
    sdata[local] = prod;

    __syncthreads();

    for (int s = blockDim.x / 2; s > 0; s /= 2) {
        if (local < s) {
            sdata[local] += sdata[local + s];
        }
        __syncthreads();
    }

    if (local == 0) {
        atomicAdd(d_C, sdata[0]);
    }
}

int main() {
    int N = 1024, num_threads = 256;
    int num_blocks = GET_NUM_BLOCKS(N, num_threads);
    int sdata_size = sizeof(int) * num_threads;

    int *h_A, *h_B, *h_C, *d_A, *d_B, *d_C;
    int bytes = sizeof(int) * N;

    h_A = (int*)malloc(bytes);
    h_B = (int*)malloc(bytes);
    h_C = (int*)malloc(sizeof(int));

    for (int i = 0; i < N; i++) {
        int tmp1 = std::rand() % 100;
        int tmp2 = std::rand() % 100;
        h_A[i] = tmp1;
        h_B[i] = tmp2;
        std::cout << i << " --- " << h_A[i] << " --- " << h_B[i] << std::endl;
    }

    CUDA_CHECK(cudaMalloc(&d_A, bytes));
    CUDA_CHECK(cudaMalloc(&d_B, bytes));
    CUDA_CHECK(cudaMalloc(&d_C, sizeof(int)));

    CUDA_CHECK(cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice));
    CUDA_CHECK(cudaMemcpy(d_B, h_B, bytes, cudaMemcpyHostToDevice));
    CUDA_CHECK(cudaMemset(d_C, 0, sizeof(int)));

    dot_product<<<num_blocks, num_threads, sdata_size>>>(d_A, d_B, d_C, N);
    CUDA_CHECK(cudaGetLastError());
    CUDA_CHECK(cudaDeviceSynchronize());

    CUDA_CHECK(cudaMemcpy(h_C, d_C, sizeof(int), cudaMemcpyDeviceToHost));

    std::cout << "result: " << *h_C << std::endl;

    free(h_A);
    free(h_B);
    free(h_C);
    CUDA_CHECK(cudaFree(d_A));
    CUDA_CHECK(cudaFree(d_B));
    CUDA_CHECK(cudaFree(d_C));

    return 0;
}
