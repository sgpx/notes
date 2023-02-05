#include <stdio.h>

int main(){
	int a, b, c = 0;
	scanf("%d", &a);
	if(a == 123)
		scanf("%d %d", &b, &c);
	else
		scanf("%d", &b);
	printf("b : %d, c : %d\n", b, c);
}
