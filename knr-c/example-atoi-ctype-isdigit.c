#include <stdio.h>
#include <ctype.h>

int my_atoi(char s[])
{
	int n = 0;
	for(int i = 0; isdigit(s[i]); i++)
	{
		int digit = s[i] - '0';
		n = (10*n) + digit;
	}
	return n;
}

int main()
{
	char a[5] = "123aa";
	int s = my_atoi(a);
	printf("%d + 1 = %d\n",s,s+1);
}
