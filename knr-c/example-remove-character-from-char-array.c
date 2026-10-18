#include <stdio.h>

int squeeze(char s[], char x)
{
	int ctr = 0;
	int ctx = 0;
	while(s[ctr] != '\0')
	{

		if(s[ctr] != x)
		{
			s[ctx] = s[ctr];
			++ctx;
		}
		++ctr;
	}
}
int main()
{
	char s[5] = "12aa3";
	squeeze(s,'a');
	printf("%s\n",s);
}
