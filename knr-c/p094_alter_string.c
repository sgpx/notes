#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int test1(){
	char *s = (char*)malloc(1000);
	strcpy(s, "hey");
	char *p = s;
	*p = 'z';
	printf("s : %s\n", s);
	printf("p : %s\n", p);
	return 0;
}

int test2(){
	char *s = (char*)malloc(1000);
	strcpy(s, "hey");
	char *p = (char*)malloc(1000);
	strcpy(p, s);
	*p = 'z';
	printf("s : %s\n", s);
	printf("p : %s\n", p);
	return 0;
}

int main(){
	test2();
}
