#include <stdio.h>

int getint(int * p){
	*p = 5;
}

int main(){
	int n, arr[10];
	for(int i = 0; i < 10; i++) getint(&arr[i]);
	for(int i = 0; i < 10; i++) printf("%d %d\n", i, arr[i]);

	return 0;
}
