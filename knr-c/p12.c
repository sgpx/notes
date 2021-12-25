#include <stdio.h>

main()
{
	int c;
	c = getchar();
	while ( c != 97 )
	{
		putchar(c);
		c = getchar();
	}
	printf("reached EOF\n");
}


// output
// x



// output
// the character was: h



// output


// output


// output


// output
// b
// d
// ef
// reached EOF
