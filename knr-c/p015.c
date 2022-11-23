#include <stdio.h>

main()
{
	int c;
	int counter;
	c = getchar();
	counter = 0;

	while(c != EOF)
	{
		putchar(c);
		printf("\nnumber of characters : %d\n", counter);
		c = getchar();
		counter++;
	}
}




// output
// 1
// 2
// 3
// 4


// output
// 1


// output
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// number of characters : 16


// output
// 1number of characters : 0
// number of characters : 12number of characters : 2
// number of characters : 33number of characters : 4
// number of characters : 5


// output
// 1number of characters : 0

// number of characters : 1
// 2number of characters : 2

// number of characters : 3
// 3number of characters : 4

// number of characters : 5


// output
// 1
// number of characters : 0


// number of characters : 1
// 2
// number of characters : 2


// number of characters : 3
// 3
// number of characters : 4


// number of characters : 5
// 4
// number of characters : 6


// number of characters : 7


// output
// 1
// number of characters : 0
// 2
// number of characters : 1
// 3
// number of characters : 2
// 4
// number of characters : 3


// number of characters : 4
