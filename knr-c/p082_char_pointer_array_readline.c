#include <stdio.h>
#include <stdlib.h>

int readlines(char *a[], int nlines){
	for(int i = 0; i < nlines; i++){
		int j = 0;
		char * ptr = (char *) malloc(1024);
		char c = getchar();
		while(c != '\n'){
			*(ptr+j) = c;
			c = getchar();
			++j;
		}

		a[i] = ptr;
		printf("a[%d] = '%s'\n", i, a[i]);
	}
}

int main(){
	char *a[5];
	readlines(a, 5);

	return 0;
}
