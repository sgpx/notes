#include <stdio.h>
#define swap(vartype,x,y) vartype tmp = x; x = y; y = tmp;

int main(){
	int a = 1;
	int b = 2;
	printf("a: %d, b: %d\n", a, b);
	swap(int, a, b);
	printf("a: %d, b: %d\n", a, b);

	return 0;
}
