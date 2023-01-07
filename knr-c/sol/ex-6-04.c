#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define KWLEN 9
#define NLEN 1000
#define WORD_NOT_FOUND -1

int x_getline(char s[]){
	char *p = s;
	while( (*p++ = getchar()) != '\n');
	//printf("%d\n", p-sWORD_NOT_FOUND);
	return p-s-1;
}

struct word {
	int occ;
	char str[1000];
} wxarray[1000];

int wxc = 0;
char line[1000];

int checkword(char s[]){
	for(int i = 0; i < wxc; i++)
		if(strcmp(s, wxarray[i].str) == 0) return i;
	return WORD_NOT_FOUND;
}

void mkword(char s[]){
	strcpy(wxarray[wxc].str, s);
	wxarray[wxc].occ = 1;
	printf("%s\n", wxarray[wxc].str);
	printf("%d\n", wxarray[wxc].occ);
	wxc += 1;
}

void procword(char s[]){
	if(strlen(s) < 1) return;
	int wpos = checkword(s);
	if(wpos == WORD_NOT_FOUND) {
		mkword(s);
	}
	else {
		wxarray[wpos].occ += 1;
	}
}

int wordcmp(struct word * w1, struct word * w2){
	//printf("%s - %s\n", w1->str, w2->str);
	//printf("%d - %d = %d\n", w2->occ, w1->occ, (w2->occ) - (w1->occ));
	return w2->occ - w1->occ;
}

int main(){
	while(x_getline(line)){
		char tmp[1000];
		tmp[0] = '\0';
		int lx = 0;
		for(int i = 0; line[i] != '\0'; i++) {
			if(isalpha(line[i])){
				tmp[lx++] = line[i];
			}
			else {
				tmp[lx] = '\0';
				procword(tmp);
				lx = 0;
				tmp[0] = '\0';
			}
		}
	}

	for(int i = 0; i < wxc; i++) {
		printf("'%s' : %d\n", wxarray[i].str, wxarray[i].occ);
	}
	int (*fn)(const void*, const void*) = (int (*)(const void*, const void*))wordcmp;

	qsort(wxarray, wxc, sizeof(struct word), fn);
	printf("====\n");
	for(int i = 0; i < wxc; i++) {
		printf("'%s' : %d\n", wxarray[i].str, wxarray[i].occ);
	}

	return 0;
}
