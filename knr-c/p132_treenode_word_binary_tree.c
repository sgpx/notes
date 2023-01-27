#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAXWORD 1000
#define MAXBUF 10

int bufc = 0;
char buf[MAXBUF];

char getch(void)
{
	return bufc > 0 ? buf[--bufc] : getchar();
}

void ungetch(char c)
{
	buf[bufc++] = c;
}

struct tnode
{
	char *word;
	int count;
	struct tnode *left;
	struct tnode *right;
};

typedef struct tnode snode;

snode *talloc(void)
{
	return (snode *)malloc(sizeof(snode));
}

void treeprint(snode *root)
{
	if(root != NULL){
		treeprint(root->left);
		printf(" '%s' (%d) ", root->word, root->count);
		treeprint(root->right);
	}
}

char * x_strdup(char * word){
	int l = strlen(word);
	char *p = (char*)malloc(l);
	strcpy(p, word);
	return p;
}

snode * addtree(snode * root, char * word){
	if(root == NULL){
		root = talloc();
		printf("setting root->word as %s\n", word);
		root->word = x_strdup(word);
		root->count = 1;
		root->left = NULL;
		root->right = NULL;
	}
	else {
		int cmp = strcmp(root->word, word);
		if(cmp > 0){
			root->right = addtree(root->right, word);
		}
		else if(cmp < 0){
			root->right = addtree(root->left, word);
		}
		else {
			root->count += 1;
		}
	}
	return root;
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

int main()
{
	snode *root;
	char word[MAXWORD];
	root = NULL;
	while (getword(word, MAXWORD) != EOF)
	{
		if (isalpha(word[0]))
		{
			root = addtree(root, word);
		}
	}
	treeprint(root);
	return 0;
}