#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

union un1 {
	int ival;
	double dval;
} u;

int main() {
	// both ival and dval occupy same space in memory
	u.ival = 5;
	//u.dval = 2.3;
	//printf("%f\n", u.dval + 1.2);
	printf("%d\n", u.ival + 5);
	return 0;
}
