#include <stdio.h>

main()
{
	char * names[20];
	char x = 'a';
	names[0] = &x;
	printf("%c\n",*names[0]);
}


// output
// a
