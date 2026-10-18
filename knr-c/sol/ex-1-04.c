#include <stdio.h>

int main(){
	int f = 0 , c = 0;
	//c = 5*(f-32)/9;
	for(c = 0; c < 110; c += 10) {
		f = ((9/5)*c) + 32;
		printf("%03d %03d\n", c, f);
	}
	return 0;
}
