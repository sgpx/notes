#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAXTOKEN 1000

#define DEBUG_MODE 1
#define DEBUG_CPRINT 1

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
	if(DEBUG_MODE)
		printf("getch\nbufc : %d\n", bufc);
	return bufc ? xbuf[bufc--] : getchar();
}

void ungetch(char c){
	if(DEBUG_MODE)
		printf("ungetch\n");
	xbuf[++bufc] = c;
}

void reset(void){
	//if(DEBUG_MODE)
	printf("resetting..\n");
	tokentype = ' ';
	token[0] = '\0';
	name[0] = '\0';
	datatype[0] = '\0';
	out[0] = '\0';
}

void dcl(void){
	if(DEBUG_MODE)
		printf("dcl\n");
	// number of pointer asterisks
	int ns;
	// count number of asterisks
	for(ns = 0; gettoken() == '*';) ns++;
	// run dirdcl()
	dirdcl();
	// put " pointer to pointer to...." ns times in out[]
	while(ns-- > 0)
		strcat(out, " pointer to");
}

void dirdcl(){
	if(DEBUG_MODE)
		printf("dirdcl\n");
	// holds output of gettoken()
	int type;

	// if tokentype is '(' call dcl()
	// dcl (checks asterisk and runs dirdcl)

	if(tokentype == '(') {
		dcl();
		if(tokentype != ')'){
			printf("error: missing ')'\n");
			reset();
		}
	}
	else if(tokentype == NAME)
		// copy token[] to name[]
		strcpy(name, token);
	else
		printf("error: expected name or dcl\n");

	// looks for parenthesis and brackets
	while( (type=gettoken()) == PARENS || type == BRACKETS )
		if(type == PARENS)
			// function returning
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
	if(DEBUG_MODE)
		printf("gettoken\n");
	char c; // input holder
	char *p = token; // pointer to token string
	while( (c=getch()) == ' ' || c == '\t'); // keep moving until non-whitespace character is found

	// if input is '('
	if(DEBUG_CPRINT)
		printf("\n\nc : %d %c\n\n", c, c);
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
		*p++ = c;
		// eliminate infinite loop error for improper input
		while( (c = getch()) != ']'){
			*p++ = c;
			if(c == EOF) return tokentype = EOF;
		}
		*p++ = c;
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

int main(){
	int gtok = gettoken();

	while( gtok != EOF ){
		if(DEBUG_MODE)
			printf("gtok : %c\n", gtok);
		// copy last token[] to datatype[]
		strcpy(datatype, token);
		out[0] = '\0';
		// run dcl() once again
		dcl();
		if(DEBUG_MODE)
			printf("tokentype : %d '%c'\n", tokentype, tokentype);
		// if tokentype is not newline then throw a syntax error
		if( tokentype != '\n' ){ printf("syntax error\n"); reset(); }
		// print sequence : name[], out[], datatype[]
		printf("%s: %s %s\n", name, out, datatype);
		gtok = gettoken();
	}

	return 0;
}

