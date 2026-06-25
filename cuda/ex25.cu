//  Goal: Given a 2D input array $A[M][N]$, calculate the sum of all elements in the array, but structure the calculation so that it requires heavy use of shared memory within each thread block to handle the partial sums efficiently.

#include <cuda_runtime.h>
#include <cstdio>
#include <cstdlib>

int main() {
	int M = 3, N = 3;
	int **A;
	A = (int**)malloc(sizeof(int*)*M);
	if(A == NULL) return 1;
	for(int i = 0; i < M; i++) {
		(A[i]) = (int*)malloc(sizeof(int)*N);
		for(int j = 0; j < N; j++) { A[i][j] = i+j; }
	}

	int **d_A;
	cudaMalloc((int**)&d_A, sizeof(int*)*M);
	for(int i = 0; i < M; i++) {
		cudaMalloc((int*)&d_A[i], sizeof(int)*N);
	}
	for(int i = 0; i < M; i++) {
		free(A[i]);
	}
	free(A);
	cudaFree(d_A);
	return 0;
}
