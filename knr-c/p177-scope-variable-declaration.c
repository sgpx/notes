/*
### Problem 2 (Easy): Lexical Scope Shadowing Hierarchy

**Difficulty:** Easy

**Description:** Write a C function demonstrating three nested block scopes where identifier `x` is shadowed at each level.

**Requirements:**
- Declare `int x = 10;` in outer scope, `int x = 20;` in middle block, and `int x = 30;` in inner block.
- Print and assert `x` at each level.
- Show outer `x` is restored when inner blocks exit.
*/

#include <stdio.h>
#include <assert.h>



void r1() {
    int x = 10;
    printf("%d\n", x);    
{
        int x = 20;   
        printf("%d\n", x);
        assert(x  == 20);
{
    int x = 30;
    assert(x == 30);
    printf("%d\n", x);    
}

}
    assert(x  == 10);
    printf("%d\n", x);    
}



int main(void) {
    r1();
    return 0;
}
