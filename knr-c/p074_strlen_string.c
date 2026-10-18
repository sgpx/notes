#include <stdio.h>

int getlength(char * s){
	int n;
	for(n = 0; *s != '\0'; s++) n++;

	return n;
}

int main(){
	char a[10] = "llollmao";
	int x =	getlength(&a[0]);

	printf("length is %d\n", x);

	return 0;
}
