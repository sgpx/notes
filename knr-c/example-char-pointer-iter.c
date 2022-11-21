#include <stdio.h>

main()
{
	char * xyz = "123";
	for(int i=0; i<3;i++)
	{
		printf("%c\n",*(xyz+i));
	}
}
