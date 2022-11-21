#include <stdio.h>

main()
{
	int linebreak, wc;
	char c;
	
	linebreak = 0;
	wc = 0;

	c = getchar();
	while(c != EOF)
	{
		c = getchar();
		if(c == ' ')
		{
			if(linebreak == 0)
			{
				linebreak = 1;
				wc++;
			}
		}
		else
		{
			linebreak = 0;			
		}
	}
	printf("\nwords : %d\n",wc);
}
