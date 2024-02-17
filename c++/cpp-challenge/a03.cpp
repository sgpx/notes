#include <cstdio>

int add_two(int a, int b){
	return a+b;
}

int sub_two(int a, int b) {
	return a-b;
}

int mul_two(int a, int b){
	return a*b;
}

int div_two(int a, int b){
	return a/b;
}

int main() {
	printf("%d %d %d %d", add_two(3,2),
	sub_two(3,2),
	mul_two(3,2),
	div_two(3,2));
	return 0;
}
