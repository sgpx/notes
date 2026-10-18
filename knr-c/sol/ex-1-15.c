#include <stdio.h>

int c2f(int c){
	return ((9/5)*c) + 32;
}

int f2c(int f){
	return (5*(f-32))/9;
}

int main(){
	int f = 0 , c = 0;
	//c = 5*(f-32)/9;
	for(c = 0; c < 110; c += 10) {
		printf("%03d %03d\n", c, c2f(c));
	}
	printf("\n\n");
	for(f = 0; f < 320; f += 20) {
		printf("%03d %03d\n", f, f2c(f));
	}

	return 0;
}
