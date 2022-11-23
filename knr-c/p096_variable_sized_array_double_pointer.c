#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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
		sprintf(p, "foobar%d", i);
		*(x+i) = p;
	}
	for(int i = 0; i < ln; i++) {
		printf("x[%d] : %s\n", i, *(x+i));
		free(*(x+i));
	}
	free(x);
}
