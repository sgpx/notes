#include <stdio.h>

int main()
{
	char c1 = '\111';
	char c2 = '\151';
	printf("'\\111' <=> '%c' <=> '%d'\n",c1,c1);
	printf("'\\151' <=> '%c' <=> '%d'\n",c2,c2);
	return 0;
}
