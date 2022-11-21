#include <stdio.h>
#include <math.h>
#include <assert.h>

int main()
{
	int x = -pow(2, 31);
	int y = x * -1;
    printf("%d %d\n", x, y);
	printf("%d %d\n", -pow(2,31), (-1)*(-pow(2,31)));
    assert(x != y);

    return 0;
}