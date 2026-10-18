#include <stdio.h>

int main()
{
	char c1 = '\x0000';
	printf("'\\x0000' <=> '%c' <=> '%d'\n", c1, c1);

	char c2 = '\x0001';
	printf("'\\x0001' <=> '%c' <=> '%d'\n", c2, c2);


	char c3 = '\x5F';
	printf("'\\x5F' <=> '%c' <=> '%d'\n", c3, c3);

	return 0;
}
