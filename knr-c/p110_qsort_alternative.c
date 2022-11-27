#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char lower(char x){
	if(x >= 'A' && x <= 'Z')
		return 'A' - x + 'a';
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
	return lower(*s) - lower(*t);
}

void printarray(char *x[]){
	printf("\n\n");
	for(int i = 0; i < 5; i++)
		printf("%d : '%s'\n", i, x[i]);
}

void swap(char *x[], int i, int j){
	char *tmp = x[i];
	x[i] = x[j];
	x[j] = tmp;
	printarray(x);
}

int part(char *x[], int low, int high){
	char * pivot = x[high];
	int i, j;
	i = low - 1;
	for(j = low; j < high; j++)
		if(strcmp(x[j], pivot) > 0)
			swap(x, ++i, j);

	swap(x, i+1, high);
	return i+1;
}

void x_qsort(char *x[], int low, int high){
	if(low >= high) return;
	int pi = part(x, low, high);
	x_qsort(x, low, pi - 1);
	x_qsort(x, pi + 1, high);
}

int main(){
	char *x[5] = {
		"pqrs",
		"abc",
		"tuvwx",
		"hjk",
		"Abc",
	};
	x_qsort(x, 0, 4);
	printarray(x);
}
