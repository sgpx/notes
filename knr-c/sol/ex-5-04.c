#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int x_strend(char * s, char * t){
	while( *s != '\0' ) ++s;
	size_t tsize = strlen(t);
	char * p = s - tsize;
	while(*p != '\0'){
		printf("s[c] : %c, t[c] : %c\n", *p, *t);
		if(*p == *t){
			++t;
			++p;
		}
		else return 0;
	}
	return 1;
}

int main(){
	int res = 0;

	char s[15] = "foobar";
	char t[5] = "bar";
	res = x_strend(s, t);
	printf("%d\n", res);

	char p[10] = "alpha";
	char q[5] = "phb";
	res = x_strend(p, q);
	printf("%d\n", res);


	return 0;

}
