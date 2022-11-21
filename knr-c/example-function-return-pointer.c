#include <stdio.h>

char * xyz()
{
	char * pqrs = "ppap";
	return pqrs;
}

int main()
{
	char * alphabeta = xyz();
	printf("%s\n",alphabeta);
	return 0;
}
