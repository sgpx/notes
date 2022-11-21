#include <stdio.h>

int main()
{
	int c, nl;
	nl = 0;
	while( (c = getchar()) != 'x')
	{
		if(c == '\n'){
			++nl;
		}
	}
	printf("number of lines : %d\n",nl);

}
