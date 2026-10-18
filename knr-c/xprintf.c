#include <stdarg.h>
#include <unistd.h>
#include <stdio.h>
typedef long long ll;

void x_putchar(char x)
{
    char a[1];
    a[0] = x;
    // a[1] = '\0';
    // write(0, a, 2);
    write(0, a, 1);
}

void xputlong(ll x)
{
    int q[1024], ctr = 0, negative = 0;
    if (x < 0)
    {
        x = -x;
        negative = 1;
    }
    while (x)
    {
        int rem = x % 10;
        q[ctr++] = rem;
        x -= rem;
        x /= 10;
    }
    if (negative)
        x_putchar('-');
    for(int i = ctr - 1; i >= 0; i--)
        x_putchar('0' + q[i]);

    x_putchar('\0');
}

void x_printf(char *fmt, ...)
{
    va_list ap;
    va_start(ap, fmt);
    char *p = fmt;
    while (*p != '\0')
    {
        // if(*p == '\n') break;

        if (*p == '%')
        {
            char c = *(p + 1);
            if (c == 'd' || c == 'u')
            {
                int lval = va_arg(ap, int);
                xputlong(lval);
                p++;
            }
            else if(c == 'p'){
                unsigned long long pval = va_arg(ap, unsigned long long);
                xputlong(pval);
                p++;
            }
            else if (c == 's')
            {
                char *sval = va_arg(ap, char *);
                char *sptr = sval;
                while (*sptr != '\0')
                    x_putchar(*sptr++);
                x_putchar('\0');
                p++;
            }
            else
                x_putchar(c);
            p++;
        }
        else
            x_putchar(*p++);
    }
    x_putchar('\0');
}