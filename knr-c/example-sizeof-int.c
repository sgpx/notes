#include <stdio.h>

int main() {
	int x1 = 1;
	short int x2 = 1;
	long int x3 = 1;
	size_t sx1 = sizeof(x1);
	size_t sx2 = sizeof(x2);
	size_t sx3 = sizeof(x3);
	printf("size of int is %lu\n", sx1);
	printf("size of short int is %lu\n", sx2);
	printf("size of long int is %lu\n", sx3);
}
