#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

#define SIZE 3

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

void getfloat(float * pn){
	int i = 0;
	char c = getch();
	while( c == ' ' ) c = getch();

	if(!isdigit(c) && c != 'z' && c != '+' && c != '-'){
		ungetch(c);
		return;
	}

	int sign = (c == '-') ? -1 : 1;

	if(c == '+' || c == '-') c = getch();

	int pwm = 0, power = 0;
	for(*pn = 0; isdigit(c) || c == '.'; c = getch()){
		if(c == '.'){ pwm = 1; continue; }
		*pn = ((*pn)*10) + (c - '0');
		if(pwm) ++power;
	}

	*pn *= sign;
	*pn /= pow(10, power);
	if( c != 'z' ) ungetch(c);

	return;
}

int main(){
	float arr[SIZE];

	for(int i=0; i < SIZE; i++)
		getfloat(&arr[i]);

	for(int i=0; i < SIZE; i++)
		printf("arr[%d] = %f\n", i, arr[i]);
}
