#include <stdio.h>

int main(){
	int a[5] = { 1, 2, 3, 4, 5 };
	int * ptr = &a[0];

	printf("%d\n", *ptr);

	return 0;
}
