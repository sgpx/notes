/*
grammar

dcl -> pointer* dirdcl

dirdcl -> (dcl)
dirdcl -> ident
dirdcl -> dirdcl[constexpr]
dirdcl -> dirdcl(param_type_list)

pointer -> asterisk type_qualifier_list*
pointer -> asterisk type_qualifier_list* pointer

type_qualifier_list -> const
type_qualifier_list -> volatile

param_type_list -> param_type* param_type_list
param_type -> unsigned* int
param_type -> float
param_type -> double
param_type -> void
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define DEBUG_LV1 1
#define DEBUG_LV2 1

enum
{
	PARENS_OPEN,
	PARENS_CLOSED,
	PARENS_BOTH,
	BRACKETS,
	NAME,
	CHARACTER,
	COMMA,
	ASTERISK,
	DATATYPE,
	TYPE_QUALIFIER,
	LINE_END
};

char token[1000];

char xline[1000];
int xctr = 0;

char token_array[100][100];
int tokentype_array[100];

int token_ctr = 0, token_sel = 0;

char current_token[100];
int current_tokentype = -1;

int z_dt_set = 0;

char z_out[100];
char z_datatype[100];
char z_name[100];

void dcl();
void dirdcl();

void x_getline(char xline[])
{
	char c;
	int i = 0;
	while ((c = getchar()) != '\n')
		xline[i++] = c;
	xline[i] = '\0';
}

char getch()
{
	return xline[xctr++];
}

void ungetch()
{
	--xctr;
}

int is_datatype(char *token)
{
	if (strcmp(token, "int") == 0)
		return 1;
	else if (strcmp(token, "long") == 0)
		return 1;
	else if (strcmp(token, "short") == 0)
		return 1;
	else if (strcmp(token, "float") == 0)
		return 1;
	else if (strcmp(token, "double") == 0)
		return 1;
	else if (strcmp(token, "char") == 0)
		return 1;
	else if (strcmp(token, "void") == 0)
		return 1;
	else if (strcmp(token, "unsigned") == 0)
		return 1;
	else
		return 0;
}

int is_type_qualifier(char *token)
{
	if (strcmp(token, "const") == 0)
		return 1;
	else if (strcmp(token, "volatile") == 0)
		return 1;
	else
		return 0;
}

int tokenize_line(char xline[])
{
	char c;
	while ((c = getch()) != '\0' && c != '\n')
	{
		if (c == ' ')
			continue;
		else if (isalpha(c))
		{
			int i = 0;
			while (isalnum(c))
			{
				token[i++] = c;
				c = getch();
			}
			token[i] = '\0';
			strcpy(token_array[token_ctr], token);
			int my_tokentype = NAME;

			if (is_datatype(token))
			{
				my_tokentype = DATATYPE;
			}
			else if (is_type_qualifier(token))
			{
				my_tokentype = TYPE_QUALIFIER;
			}
			tokentype_array[token_ctr] = my_tokentype;
			++token_ctr;
			ungetch();
			printf("token : '%s'\n", token_array[token_ctr - 1]);
		}
		else if (c == '(')
		{
			c = getch();
			if (c == ')')
			{
				strcpy(token_array[token_ctr], "()");
				tokentype_array[token_ctr] = PARENS_BOTH;
				++token_ctr;
			}
			else
			{
				ungetch();
				strcpy(token_array[token_ctr], "(");
				tokentype_array[token_ctr] = PARENS_OPEN;
				++token_ctr;
			}
		}
		else if (c == ')')
		{
			strcpy(token_array[token_ctr], ")");
			tokentype_array[token_ctr] = PARENS_CLOSED;
			++token_ctr;
		}
		else if (c == '[')
		{

			int i = 0;
			while (c != ']' && c != '\0' && c != '\n')
			{
				token[i++] = c;
				c = getch();
			}

			if (c != ']')
			{
				printf("syntax error : unterminated brackets\n");
				return 1;
			}
			else
			{
				token[i++] = c;
			}

			token[i] = '\0';
			strcpy(token_array[token_ctr], token);
			tokentype_array[token_ctr] = BRACKETS;
			++token_ctr;
			// ungetch();
			printf("token : '%s'\n", token_array[token_ctr - 1]);
		}
		else if (c == ',')
		{
			strcpy(token_array[token_ctr], ",");
			tokentype_array[token_ctr] = COMMA;
			++token_ctr;
		}
		else if (c == '*')
		{
			strcpy(token_array[token_ctr], "*");
			tokentype_array[token_ctr] = ASTERISK;
			++token_ctr;
		}
		else
		{
			printf("xctr : %d, c : %c\n", xctr, c);
			token[0] = c;
			token[1] = '\0';
			strcpy(token_array[token_ctr], token);
			tokentype_array[token_ctr] = CHARACTER;
			++token_ctr;
		}
	}
	strcpy(token_array[token_ctr], "");
	tokentype_array[token_ctr] = LINE_END;
	++token_ctr;

	return 0;
}

int check_parens()
{
	int chk2 = 0;

	for (int i = 0; i < token_ctr; i++)
	{
		printf("%d %s\n", tokentype_array[i], token_array[i]);
		if (tokentype_array[i] == PARENS_OPEN)
		{
			chk2 += 1;
		}
		else if (tokentype_array[i] == PARENS_CLOSED)
		{
			chk2 -= 1;
		}
	}
	if (chk2 != 0)
		printf("syntax error: unterminated parenthesis\n");

	return chk2;
}

void next_token()
{
	strcpy(current_token, token_array[token_sel]);
	current_tokentype = tokentype_array[token_sel];
	token_sel += 1;
	if (DEBUG_LV2)
		printf("next_token called\ncurrent_token : '%s'\nnext_token end\n\n", current_token);
}

void prev_token()
{
	token_sel -= 1;
	strcpy(current_token, token_array[token_sel]);
	current_tokentype = tokentype_array[token_sel];
}

/*

dirdcl -> ident
dirdcl -> dirdcl[constexpr]
dirdcl -> (dcl)
dirdcl -> dirdcl(param_type_list)

*/
char ptl_output[100];
int check_if_param_type_list()
{
	if (DEBUG_LV2)
		printf("check_if_param_type_list called\n");
	int is_ptl = 1;
	ptl_output[0] = '\0';
	int ctk = token_sel - 1;
	printf("check_if_param_type_list token : %s\n", token_array[ctk]);
	if (tokentype_array[ctk] == PARENS_OPEN)
	{
		strcat(ptl_output, "(");
		while (tokentype_array[ctk] != PARENS_CLOSED)
		{
			++ctk;
			if (tokentype_array[ctk] == DATATYPE || tokentype_array[ctk] == COMMA || tokentype_array[ctk] == ASTERISK || tokentype_array[ctk] == PARENS_CLOSED)
				strcat(ptl_output, token_array[ctk]);
			else
			{
				printf("found tokentype : %d\n", tokentype_array[ctk]);
				is_ptl = 0;
				break;
			}
		}
	}
	if (is_ptl)
		token_sel = ctk;
	printf("token_sel : %d\n", token_sel);
	return is_ptl;
}

void dirdcl()
{
	if (DEBUG_LV2)
		printf("dirdcl called\n");
	if (DEBUG_LV1)
		printf("dirdcl() current_tokentype : %d\n", current_tokentype);
	if (DEBUG_LV1)
		printf("dirdcl() current_token : %s\n\n\n", current_token);

	if (current_tokentype == LINE_END)
		return;
	else if (current_tokentype == NAME)
	{
		strcpy(z_name, current_token);
		next_token();
	}
	else if (current_tokentype == DATATYPE || current_tokentype == COMMA)
	{
		if (z_dt_set == 0)
		{
			z_dt_set = 1;
			strcpy(z_datatype, current_token);
		}
		else
			strcat(z_out, current_token);

		next_token();
	}


	while (current_tokentype == PARENS_OPEN || current_tokentype == PARENS_BOTH || current_tokentype == BRACKETS)
	{
		if (current_tokentype == PARENS_BOTH)
		{
			strcat(z_out, " function() returning");
		}
		else if (current_tokentype == BRACKETS)
		{
			strcat(z_out, " array");
			strcat(z_out, current_token);
			strcat(z_out, " of");
		}
		else if (current_tokentype == PARENS_OPEN)
		{
			int ptl = check_if_param_type_list();
			printf("ptl : %d\n", ptl);
			if (ptl)
			{
				if (DEBUG_LV1)
					printf("ptl_output : %s\n", ptl_output);
				strcat(z_out, " function");
				strcat(z_out, ptl_output);
				strcat(z_out, " returning");
			}
			else
			{
				dcl();
				if (current_tokentype != PARENS_CLOSED)
					printf("syntax error: unterminated parenthesis\n");
			}
		}
		next_token();
	}
}

void dcl()
{

	if (current_tokentype == LINE_END)
		return;

	next_token();

	if (DEBUG_LV2)
		printf("dcl called\n");
	if (DEBUG_LV1)
		printf("dcl() current_tokentype : %d\n", current_tokentype);
	if (DEBUG_LV1)
		printf("dcl() current_token : %s\n\n\n", current_token);

	int ast_ctr = 0;
	while (current_tokentype == ASTERISK)
	{
		++ast_ctr;
		next_token();
	}

	dirdcl();

	printf("ast_ctr : %d\n", ast_ctr);
	for (int i = 0; i < ast_ctr; i++)
		strcat(z_out, " pointer to");
}

int main()
{
	//x_getline(xline);
	//strcpy(xline, "int (*x)[13]");
	strcpy(xline, "int *x[13]");
	printf("%s\n", xline);

	int chk1 = tokenize_line(xline);
	if (chk1)
		return 1;

	int chk2 = check_parens();
	if (chk2)
		return 1;

	for (int i = 0; i < token_ctr; i++)
		printf("token %d : '%s'\n", tokentype_array[i], token_array[i]);

	do
	{
		dcl();
	} while (current_tokentype != LINE_END);

	printf("z_datatype : '%s'\n", z_datatype);
	printf("z_out : '%s'\n", z_out);
	printf("z_name : '%s'\n", z_name);
	printf("%s : %s %s\n", z_name, z_out, z_datatype);
	return 0;
}
