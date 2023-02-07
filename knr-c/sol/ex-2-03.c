#include <stdio.h>
//#include <string.h>
//#include <math.h>

typedef unsigned long long ull;

int xval(char x) {
	if(x >= 'A' && x <= 'F') return x-'A'+10;
	else if(x >= 'a' && x <= 'f') return x-'a'+10;
	else if(x >= '0' && x <= '9') return x-'0';
	else return x;
}

ull htoi(char *s) {
	char *p = s;
	if(p[0] == '0' && (p[1] == 'x' || p[1] == 'X'))
		p += 2;
	//int pw = strlen(p) - 1;
	ull rv = 0;
	while(*p != '\0') {
		int val = xval(*p);
		//rv += (pow(16, pw--) * val);
		rv *= 16;
		rv += val;
		printf("val : %d, rv : %llu\n", val, rv);
		++p;
	}
	return rv;
}

int main() {
	char s[] = "0x222F8118"; //"0x123F";
	ull res = htoi(s);
	printf("res : %llu\n", res);

	return 0;
}
