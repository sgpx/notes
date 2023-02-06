#include <stdarg.h>
#include <stdio.h>

void fxn(int nargs, ...) {
    va_list ap;
    va_start(ap, nargs);
    for (int i = 0; i < nargs; i++) {
        char *s = va_arg(ap, char *);
        printf("s : %s\n", s);
    }
    return;
}

int main() {
    // char a1[] = "sdnflasndfkas\0", a2[] = "adlkfnasldkfn\0";
    char *a1 = "sdnflasndfkas\0", *a2 = "adlkfnasldkfn\0";
    fxn(2, a1, a2);
    return 0;
}
