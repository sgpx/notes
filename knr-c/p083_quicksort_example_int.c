#include <stdio.h>
void px(int v[]){
	printf("===\np :");
	for(int i = 0; i < 5; i++) printf(" %d ", v[i]);
	printf("\n===\n");
	return;
}

void swap(int v[], int i, int j){
	printf("swapping v[%d]=%d and v[%d]=%d\n", i, v[i], j, v[j]);
	int x = v[i];
	v[i] = v[j];
	v[j] = x;
	px(v);
}

void qsort(int v[], int left, int right){
	int i, last;
	if(left >= right) return;

	swap(v, left, (left+right)/2);

	last = left;

	for(i = left+1; i <= right; i++){
		printf("i : %d, v[i] : %d\n", i, v[i]);
		if(v[i] < v[left]){
			printf("swapping %d & %d\n", last+1, i);
			swap(v, ++last, i);
		}
		px(v);
	}

	swap(v, left, last);
	qsort(v, left, last-1);
	qsort(v, left+1, right);
}


int main(){
	int v[5] = { 4, 5, 1, 3, 2 };
	px(v);
	qsort(v, 0, 4);
	px(v);
	return 0;
}
