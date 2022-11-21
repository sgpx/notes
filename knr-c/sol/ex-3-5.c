#include <stdio.h>

void reverse(char s[]){
        int i = 0, len = 0;
        while( s[len] != '\0' ) ++len;
	printf("len: %d\n", len);
        while( i < len/2 ) {
                char tmp = s[i];
                s[i] = s[len - i - 1];
                s[len - i - 1] = tmp;
		printf("swap %d %c %c\n", i, tmp, s[i]);
                ++i;
        }
}

char basefit(int x){
	if( x < 10 ) return '0' + x;
	else {
		return 'A' + x - 10;
	}
}

void itob(int n, char s[], int base){
	int sign = n >= 0 ? 1 : -1;
	unsigned int a = (unsigned int)n;

	int i = 0;

	while(a != 0){
		int rem = a % base;
		printf("rem: %d\n", rem);
		char ins = basefit(rem);

		s[i] = ins;
		++i;
		printf("ins: %c\n", ins);
		a = (a - rem) / base;
	}
	s[i] = '\0';
	printf("%s\n", s);
	reverse(s);
	printf("%s\n", s);

}
int main() {
	int n = 559;
	char a[20];
	itob(n, a, 8);
	printf("n : %d\n", n);
	printf("a : '%s'\n", a);

	return 0;
}
