#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int (*my_func)(const void*, const void*);

void x_getline(char s[]){
	char c = getchar();
	int ctr = 0;
	while( c != '\n' ){
		s[ctr++] = c;
		c = getchar();
	}
	s[ctr] = '\0';
}

int main(int argc, char *argv[]){
	char s[10][100];
	for(int i = 0; i < 10; i++) x_getline(s[i]);
	my_func fn = (my_func) strcmp;
	qsort(s, 10, sizeof(s[0]), fn);

	for(int i = 0; i < 10; i++)
		printf("s[%d] = %s\n", i, s[i]);
}
