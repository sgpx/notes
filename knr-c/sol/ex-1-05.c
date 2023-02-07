#include <stdio.h>

int main(){
	int c = 0;
	for(int f = 300; f > -20; f -= 20){
		c = 5*(f-32)/9;
		printf("%03d %03d\n", f, c);
	}
	return 0;
}
