#include <stdio.h>

void itoa(int a, char s[]){
	static int i = 0;
	if(a < 0){ s[i++] = '-'; a = -a; }

	int rem = a % 10;
	printf("a : %d, static i : %d, rem : %d\n", a, i, rem);
	if(a/10) itoa(a/10, s);
	s[i++] = '0' + rem;
	s[i] = '\0';
}

int main(){
	char s[20];
	int a = -123;
	itoa(a, s);
	printf("a: %d\n", a);
	printf("s: '%s'\n", s);

	return 0;
}
