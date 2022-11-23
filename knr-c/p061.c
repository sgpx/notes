#include <stdio.h>
#include <limits.h>

int main(){
	int a = INT_MIN;
	double d = (double)a;
	printf("a : %d\n", a);
	printf("f : %f\n", d);

	printf("a : %d\n", -a);
	printf("f : %f\n", -d);

	return 0;
}
