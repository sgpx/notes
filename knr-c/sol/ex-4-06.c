#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAXOP 100
#define NUMBER '0'
#define MAXVAL 100
#define Z_END 'z'
#define BUFSIZE 100

double stored_variable = 0;

int sp = 0;
double val[MAXVAL];

char buf[BUFSIZE];
int bufp = 0;

int getch(void){
	return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(char c){
	//printf("ungetch c : %c %d\n", c, c);

	if(bufp >= BUFSIZE) printf("error: too many characters\n");
	else buf[bufp++] = c;
}

void push(double f){
	if(sp < MAXVAL) val[sp++] = f;
	else printf("error: stack full, sp : %d\n", sp);
}

double pop(void){
	if(sp > 0) return val[--sp];
	else printf("stack empty\n");
	return 0;
}

int getop(char s[]){
	int i = 0;
	char c = getch();
	while( c == ' ' || c == '\t' ){
		c = getch();
	}

	if( !isdigit(c) && c != '.' ) return c;

	while(isdigit(c)){
		s[i++] = c;
		c = getch();
	}

	s[i] = '\0';
	if( c != Z_END ) ungetch(c);
	return NUMBER;
}

int main(){
	int type;
	double op2;
	char s[MAXOP];

	while( (type = getop(s)) != Z_END ) {
		printf("type is '%c'\n", type);
		switch(type) {
			case NUMBER:
				push(atof(s));
				break;

			case '+':
				push(pop() + pop());
				break;

			case '-':
				op2 = pop();
				push(pop() - op2);
				break;

			case '*':
				push(pop() * pop());
				break;

			case '/':
				op2 = pop();
				if(op2 != 0) push(pop() / op2);
				else printf("zero division error\n");
				break;
			case 'v':
				push(stored_variable);
				stored_variable = 0;
				break;
			case '\n':
				stored_variable = pop();
				printf("%f\n", stored_variable);
				break;
			case '%':
				op2 = pop();
				push((int) pop() % (int) op2);
				break;

			case 'l': // print top two elements of stack without popping
				printf("sp : %d\n", sp);
				if(sp >= 1){
					printf("printing top two..\n");
					int v1 = sp;
					int v2 = sp - 1;
					double e1 = val[v1];
					double e2 = val[v2];
					printf("val[%d] = %f\n", v1, e1);
					printf("val[%d] = %f\n", v2, e2);
				}
				break;
			case 's': // swap top two elements of stack without popping
				printf("sp : %d\n", sp);
				if(sp >= 1){
					printf("swapping top two..\n");
					int v1 = sp;
					int v2 = sp - 1;
					printf("%f\n", val[v1]);
					printf("%f\n", val[v2]);

					int tmp = val[v1];
					val[v1] = val[v2];
					val[v2] = tmp;
					printf("after swap..\n");
					printf("%f\n", val[v1]);
					printf("%f\n", val[v2]);

				}
				break;
			default:
				printf("unknown operator\n");
				break;
		}
	}
}
