#include <stdio.h>
#include <string.h>

int x_strcmp(char *x, char *y){
	while(*x == *y){
		if(*x == '\0') return 0;
		x++;
		y++;
	}
	return (*x)-(*y);
}

int main(){
	char *x = "lol";
	char *y = "loll";
	printf("%d\n", strcmp(x,y));
	printf("%d\n", x_strcmp(x,y));
}
