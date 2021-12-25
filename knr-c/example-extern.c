#include <stdio.h>

int a;

int foo()
{
	extern int a;
	a = 1;
	printf("foo: %d\n",a);
	a = a + 1;
	printf("foo: %d\n",a);
	return 0;
}

int main()
{
	foo();
	extern int a;
	printf("main: %d\n",a);
	return 0;
}
