#include <stdio.h>

char * foo()
{
	char c[4] = "abc";
	return &c[0];
}

main()
{
	char * x = foo();
	for(int i = 0; i < 4; i++)
	{
		printf("%d %c\n",i,*(x+i));
	}
}


// output


// output
