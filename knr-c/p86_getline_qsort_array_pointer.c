#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define ASIZE 5

void swap(char *x[], int i, int j){
	char * p = x[i];
	x[i] = x[j];
	x[j] = p;
}

void x_qsort(char *v[], int left, int right){
	printf("left : %d, right : %d\n", left, right);
	int i, last;
	if(left >= right) return;

	swap(v, left, (left+right)/2);
	last = left;

	for(i = left+1; i <= right; i++)
		if(strcmp(v[i], v[left]) < 0)
			swap(v, ++last, i);

	swap(v, left, last);
	x_qsort(v, left, last - 1);
	x_qsort(v, last+1, right);
}

void getlines(char *v[], int n){
	char c;
	for(int i = 0; i < n; i++){
		//char tmp[100];
		char * tmp = (char*) malloc(100);
		int ctr = 0;
		while( (c = getchar()) != '\n'){
			//tmp[ctr++] = c;
			*(tmp+ctr++) = c;
		}
		//tmp[ctr] = '\0';
		*(tmp+ctr) = '\0';
		//v[i] = &tmp[ctr];
		v[i] = tmp;
		printf("v[%d] = '%s'\n", i, v[i]);
	}
}
int main(){
	char * v[ASIZE];
	getlines(v, ASIZE);
	for(int i = 0; i < ASIZE; i++) printf("v[%d] = '%s'\n", i, v[i]);
	x_qsort(v, 0, ASIZE-1);
	for(int i = 0; i < ASIZE; i++) printf("v[%d] = '%s'\n", i, v[i]);
}
