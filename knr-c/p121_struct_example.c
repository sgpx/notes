#include <stdio.h>

struct point {
	int x;
	int y;
};

struct point maxpt = { 100, 100 };

struct point3d { int x; int y; int z; } p1, p2, p3;

struct rect {
	struct point pt1;
	struct point pt2;
};

struct point makepoint(int x, int y) {
	struct point tmp;
	tmp.x = x;
	tmp.y = y;
	return tmp;
};

int main() {
	struct point pt1;
	pt1.x = 1;
	pt1.y = 2;

	struct point pt2;
	pt2.x = 3;
	pt2.y = 4;

	printf("%d %d\n", maxpt.x, maxpt.y);

	p1.x = 5;
	p1.y = 6;
	p1.z = 7;

	printf("%d %d %d\n", p1.x, p1.y, p1.z);

	struct point pt3 = makepoint(10, 20);

	printf("%d %d\n", pt3.x, pt3.y);

	struct rect screen;
	screen.pt1 = pt1;
	screen.pt2 = pt2;

	printf("%d %d\n", screen.pt1.x, screen.pt1.y);
	printf("%d %d\n", screen.pt2.x, screen.pt2.y);

	struct point * pt4 = &pt3;
	printf("ptr : %d %d\n", (*pt4).x, (*pt4).y);
	printf("ptr alt : %d %d\n", pt4->x, pt4->y);

	return 0;
}
