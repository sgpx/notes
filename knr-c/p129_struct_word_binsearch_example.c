#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define NKEYS 3
#define MAXWORD 100
#define MAXBUF 1000
#define DEBUG_MODE 0

struct key {
	char *word;
	int count;
} keytab[NKEYS] = {
	{ "lmao", 0 },
	{ "lmao2", 0 },
	{ "lol", 0 },
}; // must be lexically sorted!

void ungetch(char);
char getch(void);
int getword(char *, int);
int binsearch(char *, struct key *, int);

int main(){
	int n;
	char word[MAXWORD];

	while(getword(word, MAXWORD) != EOF){
		if(isalpha(word[0]))
			if((n = binsearch(word, keytab, NKEYS)) >= 0)
				keytab[n].count++;
	}
	for(n = 0; n < NKEYS; n++){
		//if(keytab[n].count > 0)
			printf("%d : %4d %s\n", n, keytab[n].count, keytab[n].word);
	}
}

int binsearch(char * word, struct key tab[], int n){
	if(DEBUG_MODE) printf("searching for word : %s\n", word);
	int cond;
	int low, high, mid;

	low = 0;
	high = n - 1;
	if(DEBUG_MODE)
		printf("====\n");

	while(low <= high) {
		mid = (low+high) / 2;
		if(DEBUG_MODE){
			printf("low : %d, mid : %d, high : %d\n", low, mid, high);
			printf("word : %s, keytabmidword: %s, strcmp : %d\n", word, tab[mid].word, strcmp(word, tab[mid].word));
		}

		if((cond = strcmp(word, tab[mid].word)) < 0){
			high = mid - 1;	
		}
		else if(cond > 0){
			low = mid + 1;
		}
		else {
			return mid;
		}
	}
	if(DEBUG_MODE)
		printf("====\n");

	return -1;
}

int bufc = 0;
char buf[MAXBUF], *bufptr = buf;

char getch(void){
	return bufc > 0 ? buf[--bufc] : getchar();
}

void ungetch(char c){
	buf[bufc++] = c;
}

int getword(char *word, int lim){
	int c;
	char * w = word;

	while(isspace(c=getch()));

	if(c != EOF){
		*w++ = c;
	}
	if(!isalpha(c)){
		*w = '\0';
		return c;
	}
	for(; --lim > 0; w++){
		if(!isalnum(*w=getch())){
			ungetch(*w);
			break;
		}
	}
	*w = '\0';
	printf("word : %s\n", word);
	return word[0];
}
