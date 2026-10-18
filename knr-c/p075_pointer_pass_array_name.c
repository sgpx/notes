#include <stdio.h>

int getlength(char * s){
	int n;
	for(n = 0; *s != '\0'; s++) n++;

	return n;
}

int main(){
	char a[10] = "llollmao";
	int x1 = getlength(a);
	int x2 = getlength(a+2);

	printf("x1 is %d\n", x1);
	printf("x2 is %d\n", x2);

	return 0;
}
