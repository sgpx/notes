#include <stdio.h>

struct coordinate {
	int x;
	int y;
};

void add_one(int x) {
	++x;
	printf("value inside function %d\n", x);
}

void change_foo(struct coordinate t){
	t.x += 1;
	t.y += 1;
	printf("inside func foo %d %d\n", t.x, t.y);
}

void change_actual(struct coordinate *t){
	t->x += 1;
	t->y += 1;
	printf("inside func actual %d %d\n", t->x, t->y);
}

int main() {
	int a = 5;
	add_one(a);
	printf("value outside function %d\n", a);

	struct coordinate s1;
	s1.x = 1;
	s1.y = 2;
	change_foo(s1);
	printf("outside func %d %d\n", s1.x, s1.y);
	change_actual(&s1);
	printf("outside func %d %d\n", s1.x, s1.y);
	
	return 0;
}
