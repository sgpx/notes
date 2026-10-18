#include <stdio.h>
#include <assert.h>

// Write your C solution here
int modify_counter(int counter, int delta) {
    counter += delta;
    return counter;
}

int main(void) {
    // Verification harness
    int ctr = 1, delta = 4;
    int rv = modify_counter(ctr, delta);
    printf("%d %d\n", ctr, rv);
    assert(ctr == 1);
    return 0;
}
