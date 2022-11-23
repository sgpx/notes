#include <stdio.h>

void swap(char *a[], int i, int j){
	char * x = a[i];
	a[i] = a[j];
	a[j] = x;
}

int main(){
	char *a[3];
	a[0] = "hey";
	a[1] = "hi";
	a[2] = "hello";

	printf("%d %s\n", 0, a[0]);
	printf("%d %s\n", 2, a[2]);

	swap(a, 0, 2);

	printf("%d %s\n", 0, a[0]);
	printf("%d %s\n", 2, a[2]);
}
