#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXLINES 5000
#define STORSIZE 1024*5000

static char stor[STORSIZE];
static char *storptr = stor;

char * alloc(int n){
	long int used = storptr - stor;
	if(used + n < STORSIZE){
		storptr += n;
		return storptr - n;
	}
	else {
		printf("error: store full\n");
		return 0x0;
	}
}

void afree(char *x){
	// bounds check
	if(x >= stor && x <= stor + STORSIZE)
		storptr = x;
		// bring back to pointer start pos
}

int x_getline(char *s){
	char c;
	char *ref = s;
	do {
		c = getchar();
		*s++ = c;
	}
	while( c != '\n' );
	*(--s) = '\0';
	return s - ref;
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
	printf("ln : %d\n", ln);

	char *lineptr[MAXLINES];
	char s[1024];
	int len = 0, ctr = 0;
	while( (len = x_getline(s)) > 0 ){
		printf("got : '%s'\n", s);
		char * line = alloc(1024);
		strcpy(line, s);
		printf("line : '%s'\n", line);
		lineptr[ctr] = line;
		printf("lineptr : %s\n", lineptr[ctr]);
		++ctr;
	}
	printf("ctr : %d\n", ctr);
	int iter_start, iter_end;
	if(ln > ctr){
		iter_start = 0;
		iter_end = ctr;
	}
	else {
		iter_start = ctr - ln;
		iter_end = ctr;
	}
	printf("iter_start : %d\n", iter_start);
	printf("iter_end : %d\n", iter_end);
	for(int u = iter_start; u < iter_end; u++)
		printf("%d : %s\n", u, lineptr[u]);

	for(int u = 0; u < ctr; u++){
		printf("storptr : %p\n", storptr);
		printf("freeing %p\n", lineptr[u]);
		afree(lineptr[u]);
		printf("storptr : %p\n\n", storptr);
	}
}
