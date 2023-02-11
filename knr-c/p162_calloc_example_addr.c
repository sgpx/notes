#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int a;
    int b;
} elem;

int main()
{
    int n = 5;
    elem *p = calloc(n, sizeof(elem));
    for (int i = 0; i < n; i++)
    {
        p[i].a = i;
        p[i].b = i * 10;
    }
    for (int i = 0; i < n; i++)
    {
        printf("i : %d | p+i : %p, p+sz : %p,  &p[i] : %p | %d %d\n", i, p+i, p+(i*sizeof(elem)), &p[i], p[i].a, p[i].b);
    }
    // elem *q = p;
    // ++q;
    // printf("%p %p %ld\n", q, p, q-p);

    elem *q = p + 1;
    printf("%p %p %ld\n", q, p, q-p);

    free(p);
    return 0;
}