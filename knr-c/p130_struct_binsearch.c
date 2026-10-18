#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define NKEYS 3
#define MAXWORD 100
#define MAXBUF 1000
#define DEBUG_MODE 0

struct key
{
	char *word;
	int count;
};
struct key keytab[NKEYS] = {
	{"lmao", 0},
	{"lmao2", 0},
	{"lol", 0},
}; // must be lexically sorted!

void ungetch(char);
char getch(void);
int getword(char *, int);
struct key *binsearch(char *, struct key *, int);

int zmain()
{
	char *q = "lol";
	printf("binsearch");
	struct key *p = binsearch(q, keytab, NKEYS);
	printf("%d %s\n", p->count, p->word);
	return 0;
}

int main()
{
	struct key *p;
	char word[MAXWORD];

	while (getword(word, MAXWORD) != EOF)
	{
		if (isalpha(word[0]))
			if ((p = binsearch(word, keytab, NKEYS)) != NULL)
				p->count++;
	}
	for (int n = 0; n < NKEYS; n++)
	{
		// if(keytab[n].count > 0)
		printf("%d : %4d %s\n", n, keytab[n].count, keytab[n].word);
	}
	return 0;
}

struct key *binsearch(char *word, struct key *tab, int n)
{
	printf("f1\n");
	struct key *low = &tab[0];
	struct key *high = &tab[n];
	struct key *mid;
	printf("f2\n");

	while (low < high)
	{
		printf("f3\n");

		int cond;
		mid = low + (high - low) / 2;
		if ((cond = strcmp(word, mid->word)) < 0)
		{
			printf("f4\n");
			high = mid;
		}
		else if (cond > 0)
			low = mid + 1;
		else
			return mid;
	}
	printf("f5\n");
	return NULL;
}

int bufc = 0;
char buf[MAXBUF], *bufptr = buf;

char getch(void)
{
	return bufc > 0 ? buf[--bufc] : getchar();
}

void ungetch(char c)
{
	buf[bufc++] = c;
}

int getword(char *word, int lim)
{
	printf("getword\n");
	int c;
	char *w = word;

	while (isspace(c = getch()))
		;

	if (c != EOF)
	{
		*w++ = c;
	}
	if (!isalpha(c))
	{
		*w = '\0';
		return c;
	}
	for (; --lim > 0; w++)
	{
		if (!isalnum(*w = getch()))
		{
			ungetch(*w);
			break;
		}
	}
	*w = '\0';
	printf("word : %s\n", word);
	return word[0];
}
