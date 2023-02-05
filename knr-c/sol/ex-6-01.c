#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXBUF 1000
#define ETERM EOF

int bufc = 0;
char buf[MAXBUF], *bufptr = buf;

char getch(void) { return bufc > 0 ? buf[--bufc] : getchar(); }

void ungetch(char c) { buf[bufc++] = c; }

int getword(char *word, int lim)
{
	int c;
	char *w = word;
	while (isspace(c = getch()))
		;

	// string constants
	// underscores
	// comments
	// preprocessor lines

	if (c == '"')
	{
		*w++ = c;
		while ((c = getch()) != '"' && (w - word < lim))
		{
			*w++ = c;
		}
		*w++ = c;
		*w = '\0';
	}
	else if (c == '/')
	{
		*w++ = c;
		c = getch();
		if (c == '*')
		{
			*w++ = c;
			while (1)
			{
				if ((c = getch()) == '*')
				{
					*w++ = c;
					char d = getch();
					if (d == '/')
					{
						*w++ = d;
						*w++ = '\0';
						break;
					}
					else
					{
						ungetch(d);
					}
				}
				else
					*w++ = c;
			}
		}
		else if (c == '/')
		{
			*w++ = c;
			while ((c = getch()) != '\n')
				*w++ = c;
			*w = '\0';
		}
		else
		{
			ungetch(c);
			*w++ = '\0';
			return '/';
		}
	}
	else if (c == '#')
	{
		*w++ = c;
		while ((c = getch()) != '\n')
			*w++ = c;
		*w++ = '\0';
	}
	else if (c == '\'')
	{
		*w++ = c;
		while ((c = getch()) != '\'' && (w - word < lim))
		{
			*w++ = c;
		}
		*w++ = c;
		*w = '\0';
	}
	else if (isalpha(c))
	{
		*w++ = c;
		while (isalnum(c = getch()) || c == '_')
		{
			*w++ = c;
		}
		ungetch(c);
		*w = '\0';
	}
	else
	{
		*w++ = c;
		*w = '\0';
	}

	return word[0];
}

int main()
{
	char tmp[1000];
	while (getword(tmp, 1000) != ETERM)
		printf("word : %s\n", tmp);
}
