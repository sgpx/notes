#include <stdio.h>

int main(){
	int z[10];
	int * ip;
	ip = &z[0];
	*ip = 78;
	printf("ip is %p\n", ip);
	printf("value of ip is %d\n", *ip);
	printf("z[0] is %d\n", z[0]);
	return 0;
}
