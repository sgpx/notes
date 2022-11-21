#include <stdio.h>

void xiter(char * c, size_t sz)
{
	for(int i = 0; i < sz; i++)
	{
		printf("%d %c\n",i,*(c+i));
	}
}

int main()
{
	char * c = "blah";
	printf("%s\n",c);

	xiter(c,4);
}


// output
// 5


// output
// blah


// output
// blah
// 98  
// 108 
// 97 
// 104 


// output
// blah
// 0 b
// 1 l
// 2 a
// 3 h


// output
// blah
// 0 b
// 1 l
// 2 a
// 3 h


// output
// blah
// 0 b
// 1 l
// 2 a
// 3 h


// output
// blah
// 0 b
// 1 l
// 2 a
// 3 h


// output
// blah
// 0 b
// 1 l
// 2 a
// 3 h


// output
// blah
// 0 b
// 1 l
// 2 a
// 3 h


// output
// blah
// 0 b
// 1 l
// 2 a
// 3 h


// output
// blah
// 0 b
// 1 l
// 2 a
// 3 h
