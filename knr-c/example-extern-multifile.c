#include <stdio.h>
#include "example-extern-multifile-header.h"
int foo()
{
	extern int a;
	printf("foo: %d\n",a);
	a = a + 1;
	printf("foo: %d\n",a);
	return 0;
}

int main()
{
	foo();
	extern int a;
 	a = a + 3;
	printf("main: %d\n",a);
	return 0;
}
