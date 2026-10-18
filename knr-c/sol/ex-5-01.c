#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define SIZE 10

char bufc;
int bufp = 0;

void ungetch(char c){
	bufc = c;
	++bufp;
}

char getch(){
	if(bufp){
		--bufp;
		return bufc;
	}
	else {
		return getchar();
	}
}

void getint(int * pn){
	int i = 0;
	char c = getch();
	while( c == ' ' ) c = getch();

	if(!isdigit(c) && c != 'z' && c != '+' && c != '-'){
		ungetch(c);
		return;
	}

	int sign = (c == '-') ? -1 : 1;

	if(c == '+' || c == '-') c = getch();

	for(*pn = 0; isdigit(c); c = getch())
		*pn = ((*pn)*10) + (c - '0');

	*pn *= sign;

	if( c != 'z' ) ungetch(c);

	return;
}

int main(){
	int n, arr[SIZE];

	for(int i=0; i < SIZE; i++)
		getint(&arr[i]);

	for(int i=0; i < SIZE; i++)
		printf("%d\n", arr[i]);
}
