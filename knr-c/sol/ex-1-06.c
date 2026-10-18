#include <stdio.h>

int main(){
	char c;
	while((c = getchar()) != EOF){
		printf("c is not EOF : %d\n", c != EOF);
	}
	return 0;
}
