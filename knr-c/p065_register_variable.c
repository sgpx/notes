#include <stdio.h>


void fn(register int x, register int y){
	register int i = 10;

	y = (++x) * 2 * i;
	printf("%d %d %d\n", x, y, i);
}

int main(){
	fn(1, 2);
}
