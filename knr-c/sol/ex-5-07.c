#include <stdio.h>
#include <string.h>
#define MAXLINES 5
#define ALLOCSIZE 1000
#define MAXLEN 1000

char *lineptr[MAXLINES];

void swap(char *v[], int i, int j){
	char * p = v[i];
	v[i] = v[j];
	v[j] = p;
}

void qsort(char *v[], int left, int right){
	int i, last;

	if(left >= right) return;

	swap(v, left, (left+right)/2);
	last = left;

	for(i = left+1; i <= right; i++)
		if(strcmp(v[i], v[left]) < 0)
			swap(v, ++last, i);


	swap(v, left, last);
	qsort(v, left, last-1);
	qsort(v, left+1, right);

}
int x_getline(char *s, int maxlen){
	char *p = s;
	//while((*s++ = getchar()) != '\n' && (s - p) <= maxlen);
	*s = getchar();
	while(*s != '\n' && (s-p) <= maxlen){
		++s;
		*s = getchar();
	}
	*s = '\0';
	return s-p;
}

int readlines(char *lineptr[], int maxlines, char * lxptr){
	int len, nlines;
	char *p, line[MAXLEN];

	nlines = 0;
	while( (len = x_getline(line, MAXLEN)) > 0){
		if(nlines >= maxlines || (p = lxptr) == NULL)
			return -1;
		else {
			printf("line is '%s'\n", line);
			printf("line is '%s'\n", line);
			strcpy(p, line);
			lineptr[nlines++] = p;
			lxptr += (len + 1);
		}
	}

	return nlines;
}
void writelines(char *lineptr[], int nlines){
	for(int i = 0; i < nlines; i++)
		printf("%s\n", lineptr[i]);
}

int main(){
	char lxarray[ALLOCSIZE];
	int nlines;
	if( (nlines = readlines(lineptr, MAXLINES, lxarray)) >= 0){
		qsort(lineptr, 0, nlines-1);
		writelines(lineptr, nlines);
		return 0;
	}
	else {
		printf("error: input too large to sort\n");
		return 1;
	}
}
