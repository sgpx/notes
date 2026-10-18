#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

#define MAXOP 100
#define NUMBER '0'
#define MAXVAL 100
#define Z_END 'z'
#define BUFSIZE 100

double stored_variable = 0;

int ipos = 0;

int sp = 0;
double val[MAXVAL];

char buf[BUFSIZE];
int bufp = 0;
char bufc = ' ';

int getch(void){
	char res;
	if(bufp > 0){
		res = bufc;
		--bufp;
	}
	else res = getchar();

	printf("returning '%c' %d, bufp = %d\n", res, res, bufp);
	return res;
}

void ungetch(char c){
	printf("ungetch c : %c %d\n", c, c);

	if(bufp >= BUFSIZE) printf("error: too many characters\n");
	else{ bufc = c; ++bufp; };
}

void ungets(char s[]){
	printf("ungets: %s\n", s);
	int i = 0;
	while( s[i] != '\0' ){ ungetch(s[i++]); printf("ungetch %c\n", s[i]); }
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

int getop(char s[], char a[]) {
	s[0] = '\0';
	char c = a[ipos];
	int ctr = 0;
	while(a[ipos] == ' ') ipos++;

	int isnum = 0;
	if(isdigit(a[ipos])) isnum = 1;
	while( isdigit(a[ipos]) || a[ipos] == '.'){
		s[ctr++] = a[ipos++];
		printf("s : '%s'\n", s);
	}
	if(isnum){ s[ctr] = '\0'; return NUMBER; }

	while(a[ipos] == ' ') ipos++;
	if( a[ipos] == '\0' ) return '\n';
	if( !isdigit(a[ipos]) ) return a[ipos++];
}

void xgetline(char s[]){
	int i = 0;
	ipos = 0;
	char c = getchar();
	while(c != '\n'){
		s[i++] = c;
		c = getchar();
	}
	s[i++] = c;
	s[i] = '\0';
}

int zmain(){
	char s[100], a[100];
	xgetline(a);
	printf("'%s'\n", a);
	for(int x = 0; x < 5; x++) printf("type: '%c', s: '%s'\n", getop(s, a), s);
	return 0;
}
int main(){
	int type;
	double op2;
	char s[MAXOP];
	char a[MAXOP];
	xgetline(a);

	while( (type = getop(s, a)) != Z_END ) {
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
			case 's':
				op2 = pop();
				push(sin(op2 * M_PI/180));
				break;
			case 'e':
				op2 = pop();
				push(exp(op2));
				break;
			case 'p':
				op2 = pop();
				push(pow(pop(), op2));
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
			case 'w': // swap top two elements of stack without popping
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
