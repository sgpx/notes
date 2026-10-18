#include <stdio.h>

int strindex(char s[], char x)
{
	int ctr = 0;
	int rv = -1;
	while( s[ctr] != '\0' )
	{
		if(s[ctr] == x)
		{
			rv = ctr;
		}
		++ctr;
	}
	return rv;
}

int main()
{

	char s[5] = "xayay";
	char x = 'y';
	int a = strindex(s,x);
	printf("%c : %d\n",x,a);

	return 0;

}


// output
// a : 3


// output
// y : 4


// output
// y : 4
