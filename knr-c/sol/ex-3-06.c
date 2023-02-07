/*
https://stackoverflow.com/questions/22268815/absolute-value-of-int-min

The %d conversion specifier in the format string of printf converts the corresponding argument to a signed decimal integer, which in this case, overflows for the int type. C standard specifically mentions that signed integer overflow is undefined behaviour. What you should do is to use %u in the format string.
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>

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

void itoa(int n, char s[], int width){
	int i = 0;
	int sign = (n >= 0) ? 1 : -1;

	n = n < 0 ? -n : n;

	unsigned int a = (unsigned int)n;
	printf("a : %u\n", a);
	do {
		s[i++] = (a % 10) + '0';
	}
	while( (a /= 10) > 0);
	printf("s : %s\n", s);

	int diff = width - i;
	printf("diff : %d\n", diff);

	while(diff > 0){
		s[i++] = '0';
		--diff;
	}

	if(sign < 0){
		s[i++] = '-';
	}
	s[i] = '\0';
	printf("s : %s\n", s);
	reverse(s);
}

int test2(){
	int x = -411;
	char a[20] = "lmao";
	itoa(x, a, 10);

	printf("a is '%s'\n", a);
	return 0;
}

int main(){
	test2();
}
