#include <cuda_runtime.h>
#include <cstdio>
#include <cstdlib>

int main() {
    int M = 3, N = 3;
    
    // Allocate and initialize host memory
    int **A = (int**)malloc(sizeof(int*)*M);
    if(A == NULL) return 1;
    for(int i = 0; i < M; i++) {
        A[i] = (int*)malloc(sizeof(int)*N);
        for(int j = 0; j < N; j++) { 
            A[i][j] = i+j; 
        }
    }

    // Allocate device memory for row pointers
    int **d_A;
    cudaMalloc((void**)&d_A, sizeof(int*)*M);
    
    // Allocate device memory for each row and copy data
    for(int i = 0; i < M; i++) {
        int *d_row;
        cudaMalloc((void**)&d_row, sizeof(int)*N);
        cudaMemcpy(d_row, A[i], sizeof(int)*N, cudaMemcpyHostToDevice);
        cudaMemcpy(&d_A[i], &d_row, sizeof(int*), cudaMemcpyHostToDevice);
    }

    // Clean up host memory
    for(int i = 0; i < M; i++) {
        free(A[i]);
    }
    free(A);
    
    // Clean up device memory
    for(int i = 0; i < M; i++) {
        int *d_row;
        cudaMemcpy(&d_row, &d_A[i], sizeof(int*), cudaMemcpyDeviceToHost);
        cudaFree(d_row);
    }
    cudaFree(d_A);
    
    return 0;
}
