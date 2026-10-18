#include <stdio.h>
#define csize 1000
foo(char x[], int len)
{
	int ctr = 0;
	while(ctr < len)
	{
		x[ctr] = 'f';
		++ctr;
	}
	x[ctr] = '\0';
	printf("x is %s\n",x);
}
main()
{
	char cl[csize];
	foo(cl,5);	
	printf("cl is %s\n",cl);
}
