#include <stdio.h>

struct point { int x; int y; }; 

struct point makepoint(int x, int y){
	struct point tmp = { x, y };
	return tmp;
}

int main(){
	struct point a = makepoint(5, 6);
	printf("%d %d\n", a.x, a.y);
}
