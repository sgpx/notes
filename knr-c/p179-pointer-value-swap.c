/*

Description: Implement void swap_integers(int *a, int *b) in C using dereference and address-of operators.

Requirements:

    Check neither pointer is NULL.
    Swap values using dereference *.
    Invoke from caller using address-of & on stack variables.


*/

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void swap_integers(int *a, int *b) {
    if(a == NULL || b == NULL) return;
    int tmp = *b;
    *b = *a;
    *a = tmp;
}

int main() {
    int a = 1, b = 2;
    swap_integers(&a, &b);
    return 0;
}
