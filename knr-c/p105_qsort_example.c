#include <stdio.h>
#include <string.h>

void swap(char *x[], int i, int j){
	char * tmp = x[i];
	x[i] = x[j];
	x[j] = tmp;
}

void x_qsort(char *v[], int left, int right){
	int i, last;
	if(left >= right) return;

	swap(v, left, (left+right)/2 );
	last = left;
	for(i = left+1; i <= right; i++)
		if(strcmp(v[i], v[left]) < 0)
			swap(v, ++last, i);

	swap(v, left, last);
	x_qsort(v, left, last-1);
	x_qsort(v, last+1, right);
}

int main(){
	char *x[5] = { "foo", "bar", "barr", "baz", "fooo" };
	x_qsort(x, 0, 4);
	for(int i = 0; i < 5; i++)
		printf("%d %s\n", i, x[i]);
}
