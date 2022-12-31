#include <stdio.h>

const int f1(const int a, const int b){
	return a+b;
}

int main(){
	const int (*fn)(const int, const int) = &f1;
	int y = fn(1, 2);
	printf("%d\n", y);
	return 0;
}
