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
        printf("%p %p %d %d\n", p+(i*sizeof(elem)), &p[i], p[i].a, p[i].b);
    }

    free(p);
    return 0;
}