#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// TODO: Implement void scale_value(int *val, int factor)
void scale_value(int *val, int factor) {
    *val = (*val)*factor;
}

int main() {
    int val = 5, factor = 2;
    scale_value(&val, factor);
    printf("%d\n", val);
    return 0;
}
