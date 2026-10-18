#include <stdio.h>

int main(){
	const char s[10] = "lol";
	char const * p = s;
	char const * const * q = &p;
	printf("%s\n", *q);
}
