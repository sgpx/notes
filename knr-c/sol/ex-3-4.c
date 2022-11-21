/*
https://stackoverflow.com/questions/22268815/absolute-value-of-int-min

The %d conversion specifier in the format string of printf converts the corresponding argument to a signed decimal integer, which in this case, overflows for the int type. C standard specifically mentions that signed integer overflow is undefined behaviour. What you should do is to use %u in the format string.
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

int test1(){
	int x = -1 * pow(2,31);
	unsigned int y = abs(x);

	printf("%d\n", x);
	printf("%u\n", y);

	return 0;
}

void reverse(char s[]){
	int i = 0, len = 0;
	while( s[len] != '\0' ) ++len;
	while( i < len/2 ) {
		char tmp = s[i];
		s[i] = s[len - i - 1];
		s[len - i - 1] = tmp;
		++i;
	}
}

void itoa(int n, char s[]){
	int i = 0;
	int sign = (n >= 0) ? 1 : -1;
	n = n < 0 ? -n : n;
	unsigned int a = (unsigned int)n;
	do {
		s[i++] = (a % 10) + '0';
	}
	while( (a /= 10) > 0);

	if(sign < 0){
		s[i++] = '-';
	}
	s[i] = '\0';
	reverse(s);
}

int test2(){
	printf("%d\n", INT_MIN);
	int x = INT_MIN;
	char a[20] = "lmao";
	itoa(x, a);

	printf("a is '%s'\n", a);
	return 0;
}

int test3(){
	int x = INT_MIN;
	unsigned int y = (unsigned int)x;
	printf("%d %u\n", x, y);
	return 0;
}

int main(){
	test2();
}
