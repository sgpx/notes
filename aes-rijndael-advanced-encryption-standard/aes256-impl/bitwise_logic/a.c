#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int rightmost_bit(int x){
	return x & 1;
}

int rightmost_bit_alt(int x){
	return !((x|1) - x);
}

int rightmost_bit_alt_two(int x){
	return -(!x);
}


int main(){
	for(int i = 1; i < 10; i++) {
		printf("===\n%d\n", i);
		printf("%d\n", rightmost_bit(i));
		printf("%d\n", rightmost_bit_alt(i));
		printf("%d\n", rightmost_bit_alt_two(i));
	}
}
