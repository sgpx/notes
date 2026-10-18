#include <stdio.h>

int main(){
	char * a = "heyheyhey";
	printf("%s\n", a);
	printf("%p\n", a);
	printf("%p\n", &a);

	for(int i = 0; i < 9; i++) printf("%c %p\n", *(a+i), a+i);

	return 0;
}
