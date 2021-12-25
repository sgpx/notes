#include <stdio.h>


void iter(char s[])
{
	int ctr = 0;
	while(s[ctr] != '\0')
	{
		printf("%c ",s[ctr]);
		++ctr;
	}
	printf("\n");
}


void xiter(char p[])
{
	iter(p);
}

int main()
{
	char x[3] = "abc";
	char y[4] = "def";
	printf("%s\n",x);
	printf("%s\n",y);

	iter(x);
	iter(y);
}
