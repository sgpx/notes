#include <stdio.h>

int main(){
        int a = 5;
        int *x = &a;
        int *y = x + 1;
        printf("y : %p\nx : %p\ny-x : %lu\nly-lx : %lu\n", y, x, y - x, (long)y - (long)x);
        return 0;
}
