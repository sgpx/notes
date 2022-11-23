#include <stdio.h>
#include <string.h>
#define ALLOCSIZE 1000

static char allocbuf[ALLOCSIZE];
static char *allocp = allocbuf;

char * alloc(int n){
	//if(allocp - allocbuf + n <= ALLOCSIZE)
	if(allocbuf - allocp + ALLOCSIZE >= n) {
		allocp += n;
		return (allocp - n);
	}
	else return 0;
}

void afree(char *p){
	if(p >= allocbuf && p < allocbuf + ALLOCSIZE)
		allocp = p;
}

int main(){
	char *x = alloc(10);
	strcpy("lmao", x);
	printf("%s %p %p %p\n", x, x, allocp, allocbuf);

	afree(x);
	printf("%p %p\n", allocp, allocbuf);

}
