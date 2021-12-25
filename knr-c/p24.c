#include <stdio.h>
// print input one word per line
main()
{
	char c;
	c = getchar();
	while(c != EOF)
	{
		if(c == ' ')
		{
			putchar('\n');
		}
		else { 
			putchar(c);
		}
		c = getchar();
	}

}


// output
// dfsdfsldf
// afdalkjfks
// jkfajdskfj
// a
// dsfsdfsjl


// output
// abc
// def
// ghi
// jkl
// mno
// pqrs
