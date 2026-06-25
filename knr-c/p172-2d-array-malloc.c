#include <stdio.h>
#include <stdlib.h>

int main() {
	int M = 3, N = 3;
	int **A;
	A = (int**)malloc(sizeof(int*)*M);
	if(A == NULL) return 1;
	for(int i = 0; i < M; i++) {
		(A[i]) = (int*)malloc(sizeof(int)*N);
		for(int j = 0; j < N; j++) { A[i][j] = 0; }
	}

	for(int i = 0; i < M; i++) {
		free(A[i]);
	}
	free(A);
	return 0;
}
