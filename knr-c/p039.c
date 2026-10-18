#include <stdio.h>

void lowercase(char a[])
{
	int ctr = 0;
	while(a[ctr] != '\0')
	{
		char s = a[ctr];
		if( s >= 'A' && s <= 'Z' )
		{
			int char_diff = s - 'A';
			int lowercase_eq = 'a' + char_diff;
			printf("%c", lowercase_eq);
			a[ctr] = lowercase_eq;
		}
		else {
			printf("%c", s);
		}
		++ctr;
	}
	printf("\n");
}

main()
{
	char a[5] = "ABCDE";
	printf("a is %s\n",a);
	lowercase(a);
	printf("a is %s\n",a);
}


// output


// output


// output


// output


// output


// output
// ABCDEa is ABCDE


// output
// a is ABCDE
// ABCDEa is ABCDE


// output
// a is ABCDE
// abcde
// a is abcde
