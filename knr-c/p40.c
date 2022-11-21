#include <stdio.h>

int hex_to_base10(char hx[])
{
	int res = 0;
	int ctr = 0;

	while(hx[ctr] != '\0')
	{
		char s = hx[ctr];
		int tmp = 0;
		if( s >= '0' && s <= '9')
		{
			tmp = s - '0';
		}
		if( s >= 'A' && s <= 'F' )
		{
			tmp = s - 'A' + 10;
		}
		res = (16*res) + tmp;
		++ctr;
	}
	return res;
}

int main()
{
	char hex_digit[3] = "2AB";
	int int_value = hex_to_base10(hex_digit);
	printf("int value of hex %s is %d\n", hex_digit, int_value);
}


// output


// output
// int value of hex 2AB is 0


// output
// int value of hex 2AB is 311


// output
// int value of hex 2AB is 683
