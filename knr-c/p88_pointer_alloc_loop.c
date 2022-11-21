#include <stdio.h>
#define ALLOCSIZE 1000

static char allocbuf[ALLOCSIZE];
static char *allocp = allocbuf;

char *alloc(int n){
	if( allocbuf + ALLOCSIZE - allocp >= n){
		allocp += n;
		return allocp - n;
	}
	else
		return 0;
}

void afree(char *p){
	if(p >= allocbuf && p < allocbuf + ALLOCSIZE)
		allocp = p;
}

int main(){
	for(int i = 0; i < 100; i++){
		char *x = alloc(10);
		printf("%p\n", x);
	}

	return 0;
}
