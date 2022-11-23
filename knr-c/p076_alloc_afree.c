#include <stdio.h>
#define ALLOCSIZE 1000

static char allocbuf[ALLOCSIZE];
static char * allocp = allocbuf;

char * alloc(int n){
	if(allocbuf + ALLOCSIZE - allocp >= n) {
		allocp += n;
		return (allocp - n);
	}
	else return 0;
}

void afree(char * p){
	if( p >= allocbuf && p < allocbuf + ALLOCSIZE)
		allocp = p;
}

int main(){
	printf("allocp : %p\n", allocp);

	alloc(20);
	printf("allocp : %p\n", allocp);

	char * a = "abcde";
	afree(a);

	afree("lmao");
	printf("allocp : %p\n", allocp);

	return 0;
}
