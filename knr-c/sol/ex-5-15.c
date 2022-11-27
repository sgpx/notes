#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAXLEN 1000
#define MAXLINES 1000
#define BUFSIZE 100000

typedef int (*fx)(const void*, const void*);

static char allocbuf[BUFSIZE];
static char * allocp = allocbuf;

int numcmp(char *s, char *t){
	double ds = atof(s);
	double dt = atof(t);
	printf("%f %f %f\n", ds, ds, ds - dt);
	return ds - dt;
}

char * alloc(int n){
	return (char*)malloc(n);
	/*
	if(allocp + n < allocbuf + BUFSIZE){
		allocp += n;
		return allocp - n;
	}
	*/
}

char lower(char x){
	if(x >= 'A' && x <= 'Z')
		return x - 'A' + 'a';
	else
		return x;
}

int strcmp_fold(char *s, char *t){
	while(lower(*s) == lower(*t)){
		if(*s == '\0')
			return 0;
		++s;
		++t;
	}
	printf("%c %c %c %c %d\n", *s, *t, lower(*s), lower(*t), lower(*s)-lower(*t));
	return lower(*s) - lower(*t);
}


int x_getline(char *s, int len){
	char *p = s;
	do {
		*s = getchar();
		if(*s == '\n') break;
		++s;
	}
	while((s - p) < len);
	*s = '\0';
	printf("got : %s\nlen : %ld\n", p, s - p);
	return (s - p);
}

void writelines(char *lineptr[], int nlines){
	printf("===\n");
	for(int i = 0; i < nlines; i++)
		printf("%s\n", lineptr[i]);
}

void swap(char *v[], int i, int j){
	char *tmp = v[i];
	v[i] = v[j];
	v[j] = tmp;
}

void x_qsort(char *v[], int left, int right, int dir, fx fc){
	if(left >= right) return;

	int i, last;
	int mid = (left + right)/2;
	swap(v, left, mid);
	last = left;
	for(i = left + 1; i <= right; i++)
		if(dir == 0 && fc(v[i], v[left]) < 0)
			swap(v, ++last, i);
		else if(dir == 1 && fc(v[i], v[left]) > 0)
			swap(v, ++last, i);
	swap(v, left, last);
	x_qsort(v, left, last-1, dir, fc);
	x_qsort(v, last+1, right, dir, fc);
}

int readlines(char *lineptr[], int maxlines){
	int len, nlines;
	char *p, line[MAXLEN];

	nlines = 0;
	while((len = x_getline(line, MAXLEN)) > 0){
		printf("line : '%s'\nlen : %d\n", line, len);
		p = alloc(len);
		if( nlines >= maxlines || p == NULL){
			return -1;
		}
		else {
			line[len] = '\0';
			strcpy(p, line);
			lineptr[nlines++] = p;
		}
	}
	return nlines;
}

int main(int argc, char *argv[]){
	int numeric = 0, dir = 0, fold = 0;
	for(int i = 1; i < argc; i++)
		if(strcmp(argv[i], "-n") == 0)
			numeric = 1;
		else if(strcmp(argv[i], "-r") == 0)
			dir = 1;
		else if(strcmp(argv[i], "-f") == 0)
			fold = 1;

	fx fn;
	if(numeric == 1)
		fn = (fx) numcmp;
	else {
		if(fold == 1) fn = (fx) strcmp_fold;
		else fn = (fx) strcmp;
	}
	char *lineptr[MAXLINES];
	int nlines;
	nlines = readlines(lineptr, MAXLINES);
	if(nlines > 0){
		writelines(lineptr, nlines);
		x_qsort(lineptr, 0, nlines-1, dir, fn);
		writelines(lineptr, nlines);
	}
}

