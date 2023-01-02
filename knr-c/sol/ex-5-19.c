#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAXTOKEN 1000

enum { NAME, PARENS, BRACKETS };

void dcl(void);
void dirdcl(void);
int gettoken(void);
int tokentype;
char token[MAXTOKEN];
char name[MAXTOKEN];
char datatype[MAXTOKEN];
char out[MAXTOKEN];
char xbuf[MAXTOKEN];

int bufc = 0;

char getch(void){
	return bufc ? xbuf[bufc--] : getchar();
}

void ungetch(char c){
	xbuf[++bufc] = c;
}

void dcl(void){
	// number of pointer asterisks
	int ns;
	// count number of asterisks
	for(ns = 0; gettoken() == '*';) ns++;
	// run dirdcl()
	dirdcl();
	// put " pointer to pointer to...." ${ns} times in out[]
	while(ns-- > 0)
		strcat(out, " pointer to");
}

void dirdcl(){
	// holds output of gettoken()
	int type;

	// if tokentype is '(' call dcl()
	// dcl (checks asterisk and runs dirdcl)

	if(tokentype == '(') {
		dcl();
		if(tokentype != ')')
			printf("error: missing closing parenthesis ') \n");
	}
	else if(tokentype == NAME)
		// copy token[] to name[]
		strcpy(name, token);
	else
		printf("error: expected name or dcl\n");

	// looks for parenthesis and brackets
	while( (type=gettoken()) == PARENS || type == BRACKETS )
		if(type == PARENS)
			// put "function returning" to out[]
			strcat(out, " function returning");
		else {
			// if token is brackets
			// put "array" to out[]
			strcat(out, " array");
			// copy token[] to out[]
			strcat(out, token);
			// put "of" in out[]
			strcat(out, " of");
		}
	return;
}

int gettoken(void){
	char c; // input holder
	char *p = token; // pointer to token string
	while( (c=getch()) == ' ' || c == '\t'); // keep moving until non-whitespace character is found

	// if input is '('
	if(c == '('){
		// if subsequent input is ')'
		if( (c = getch()) == ')' ) {

			// copy "()" to token[]
			strcpy(token, "()");
			// return PARENS
			// set tokentype as PARENS
			return tokentype = PARENS;
		}
		else {
			// else
			// push back the input
			// set tokentype as '(' and return '('
			ungetch(c);
			return tokentype = '(';
		}
	}

	else if (c == '[') {
		// if input is '['
		// store input characters in token[] via *p until ']' is found
		for(*p++ = c; (*p++ = getch()) != ']'; );
		*p = '\0';
		// set tokentype as BRACKETS
		// return BRACKETS
		return tokentype = BRACKETS;
	}
	else if(isalpha(c)) {
		// if input is an alphabet
		// stores characters in token[] via *p, until a non alphanumeric character is found
		for(*p++ = c; isalnum(c = getch()); ) *p++ = c;
		*p = '\0';
		// push back input non-alphanumeric character
		ungetch(c);
		// set tokentype as NAME
		// return NAME
		return tokentype = NAME;
	}
	else {
		// set tokentype as character
		// return character
		return tokentype = c;
	}
}

void xproc(char s[]){
	char c, t[MAXTOKEN];
	t[0] = '(';
	t[1] = '*';
	t[2] = '*';
	for(int i = 2; s[i] != '\0'; i++)
		t[i+1] = s[i];
	strcpy(s, t);
}

int main(){

	int type;
	char temp[MAXTOKEN];

	while( gettoken() != EOF ){
		strcpy(out, token);
		printf("type : %c %d\n", type, type);
		while( (type = gettoken()) != '\n')
		if(type == PARENS || type == BRACKETS) {
			strcat(out, token);
			printf("token : %s\n", token);
		}
		else if(type == '*') {
			if(out[0] == '(' && out[1] == '*') {
				xproc(out);				
			}
			else {
				sprintf(temp, "(*%s)", out);
				strcpy(out, temp);
			}
		}
		else if(type == NAME) {
			sprintf(temp, "%s %s", token, out);
			strcpy(out, temp);
		}
		else if(type == '\n')
			continue;
		else {
			printf("invalid input at %s\n", token);
		}
	}
	printf("out : '%s'\n", out);
	printf("temp : '%s'\n", temp);
	return 0;
}

