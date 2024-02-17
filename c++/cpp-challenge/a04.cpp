#include <cstdio>

int factorial(int a){
	if(a == 0 || a == 1) return 1;
	else {
		int b = 1;
		while(a > 0) {
			b *= a--;
		}
		return b;
	}
}

int main() {
	printf("%d\n", factorial(5));
	return 0;
}
