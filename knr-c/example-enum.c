// enum is a list of integer constants
#include <stdio.h>
enum state { ON = 3, OFF = 4 };

int main()
{
	enum state x = ON;
	printf("ON is %d\n",x);
	x = OFF;
	printf("OFF is %d\n",x);

	return 0;
}
