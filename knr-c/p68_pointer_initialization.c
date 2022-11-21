#include <stdio.h>

int main(){
	int z = 0;
	int * ip;
	ip = &z;
	*ip = 5;
	printf("ip is %p\n", ip);
	printf("value of ip is %d\n", *ip);
	printf("z is %d\n", z);
	return 0;
}
