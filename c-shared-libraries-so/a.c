#include <stdio.h>

extern int foo(int x);
extern int bar;
int main()
{
	printf("%d\n",foo(bar * 5));
	return 0;
}
