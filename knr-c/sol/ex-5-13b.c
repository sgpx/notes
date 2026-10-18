#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int x_getline(char *s){
	char c;
	char *p = s;
	while( (c = getchar()) != '\n' ){
		*s++ = c;
	}
	*s = '\0';
	return s - p;
}

int main(int argc, char *argv[]){
	int ln = 5;
	if(argc >= 2){
		char * tmp = argv[1];
		char s1 = *tmp;
		if(s1 == '-'){
			++tmp;
			ln = atoi(tmp);
		}
	}

	char **x = (char **)malloc(ln * 1024);
	for(int i = 0; i < ln; i++){
		char *p = (char *)malloc(1024);
		int len = x_getline(p);
		printf("length : %d\n", len);
		if(len < 1){ ln = i + 1; break; }
		*(x+i) = p;
	}
	printf("ln : %d\n", ln);
	int stp = ln <= 5 ? 0  : ln - 5;

	for(int i = stp; i < ln; i++) {
		printf("x[%d] : %s\n", i, *(x+i));
	}
	for(int i = 0; i < ln; i++) {
		free(*(x+i));
	}

	free(x);
}

