#include <stdio.h>
#define ARRAY_LENGTH 10

void array_print(int x[], int last) {
	for(int i = 0; i < last; i++)
		printf("%d ", x[i]);
	printf("\n");	
}

void array_delete_at(int x[], int pos, int num_elem) {
	for(int i = pos; i < num_elem; i++){
		x[i] = x[i+1];
	}
}

int main() {
	int x[ARRAY_LENGTH] = { 1,6,7,8,9 };
	int num_elem = 5;
	array_print(x, num_elem);
	array_delete_at(x, 2, num_elem);
	array_print(x, num_elem-1);
}
