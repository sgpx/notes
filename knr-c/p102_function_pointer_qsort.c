#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINES 5000
#define ALLOCSIZE 5000
#define MAXLEN 1000

static char allocbuf[ALLOCSIZE];
static char *allocp = allocbuf;

char *alloc(int n){
	if(allocp + n < allocbuf + ALLOCSIZE){
		allocp += n;
		return allocp - n;
	}
	else return 0;
}

void afree(char *p){
	if(p >= allocbuf && p <= allocbuf + ALLOCSIZE)
		allocp = p;
}


char *lineptr[MAXLINES];

int numcmp(char *s1, char *s2){
	double v1, v2;

	v1 = atof(s1);
	v2 = atof(s2);

	if(v1 < v2)
		return -1;
	else if(v1 > v2)
		return 1;
	else
		return 0;
}

int x_getline(char *s, int len){
	char *p = s;
	while( (*(s++) = getchar()) != '\n');
	*(--s) = '\0';
	printf("xgt: '%s'\n", p);
	return s-p;
}

/*
int x_getline(char s[], int len){
	int i = 0;
	while(i < len){
		char c = getchar();
		if(c == '\n') break;
		s[i++] = c;
	}
	s[++i] = '\0';
	printf("s : %s\ni : %d\n", s, i);
	return i;
}
*/
int readlines(char *lineptr[], int maxlines){
	int len, nlines;
	char *p, line[MAXLEN];

	nlines = 0;
	while( (len = x_getline(line, MAXLEN)) > 0){
		printf("readlines len : %d\n", len);
		p = alloc(len+1);
		if(nlines >= maxlines || p == NULL){
			printf("terminating readlines()..\n");
			return -1;
		}
		else {
			//line[len-1] = '\0';
			strcpy(p, line);
			lineptr[nlines++] = p;
		}
	}
	return nlines;
}

void writelines(char *lineptr[], int nlines){
	printf("writeline nlines : %d\n", nlines);
	int i;
	for(i = 0; i < nlines; i++)
		printf("writeline %d : %s\n", i, lineptr[i]);
}

void swap(void *v[], int i, int j){
	void *temp;

	temp = v[i];
	v[i] = v[j];
	v[j] = temp;
}

void x_qsort(void *v[], int left, int right, 
	int (*comp) (void*, void*)) {
	int i, last;
	if(left >= right) return;

	swap(v, left, (left+right)/2 );
	last = left;
	for(i = left+1; i <= right; i++)
		if((*comp)(v[i], v[left]) < 0)
			swap(v, ++last, i);	

	swap(v, left, last);
	x_qsort(v, left, last-1, comp);
	x_qsort(v, last+1, right, comp);
}

int main(int argc, char *argv[]){
	int nlines;
	int numeric = 0;
	if( argc > 1 && strcmp(argv[1], "-n") == 0 )
		numeric = 1;
	if( (nlines = readlines(lineptr, MAXLINES)) > 0){
		for(int u=0; u < nlines; u++)
			printf("%d %s\n", u, lineptr[u]);
		int (*fn1) (void*, void*) = 
			(int (*) (void*, void*)) numcmp;

		int (*fn2) (void*, void*) = 
			(int (*) (void*, void*)) strcmp;

		int (*fnx) (void*, void*) = (numeric ? fn1 : fn2);

		x_qsort((void**) lineptr, 0, nlines-1, fnx);
		writelines(lineptr, nlines);
		return 0;
	}
	else {
		printf("error: input too big\n");
		return 1;
	}
	return 0;
}
