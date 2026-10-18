#include <stdio.h>
#include <ctype.h>
#include <stdarg.h>
#include <stdlib.h>

int isprefmtchar(char c)
{
	if (c == '.')
		return 1;
	else if (c == '-' || c == '+')
		return 1;
	else if (c >= '0' && c <= '9')
		return 1;
	else
		return 0;
}

void minprintf(char *fmt, ...)
{
	va_list ap;
	va_start(ap, fmt);
	int nchars_printed = 0;
	for (char *p = fmt; *p != '\0'; p++)
	{
		if (*p != '%')
		{
			++nchars_printed;
			putchar(*p);
		}
		else
		{
			++p;
			if (*p == '%')
			{
				putchar('%');
			}
			else
			{
				char *xfmt = malloc(30);
				char *xf = xfmt, *xf2 = malloc(30);
				while (isprefmtchar(*p))
					*(xf++) = *(p++);
				*xf = '\0';
				// printf("\n\n===\nminprintf fmt : %%%s%c\n===\n", xf, *p);
				sprintf(xf2, "%%%s%c", xfmt, *p);
				char dtype = *p;
				if (dtype == 'd' || dtype == 'i')
				{
					int ival = va_arg(ap, int);
					nchars_printed += printf(xf2, ival);
				}
				else if(dtype == 's'){
					char *cptr = va_arg(ap, char*);
					printf("%s", cptr);
				}
				else if (dtype == 'n')
				{
					int *ipval = va_arg(ap, int *);
					printf("ipval : %p, ncp : %d\n", ipval, nchars_printed);
					*ipval = nchars_printed;
				}
				else if (dtype == 'c')
				{
					char cval = va_arg(ap, int);
					nchars_printed += printf(xf2, cval);
				}
				else if (dtype == 'f' || dtype == 'a' || dtype == 'A' || dtype == 'g' || dtype == 'G' || dtype == 'E')
				{
					double dval = va_arg(ap, double);
					nchars_printed += printf(xf2, dval);
				}
				else if (dtype == 'p')
				{
					void *ptr = va_arg(ap, void *);
					nchars_printed += printf(xf2, ptr);
				}
				else if (dtype == 'u' || dtype == 'x' || dtype == 'X' || dtype == 'o')
				{
					unsigned uval = va_arg(ap, unsigned);
					nchars_printed += printf(xf2, uval);
				}
				else if (dtype == 'l')
				{
					while (*p == 'l'){
						++p;
						sprintf(xf2, "%sl", xf2);
					}
					if (*p == 'u')
					{
						sprintf(xf2, "%su", xf2);
						unsigned long long ullval = va_arg(ap, unsigned long long);
						nchars_printed += printf(xf2, ullval);
					}
					else if (*p == 'd')
					{
						sprintf(xf2, "%sd", xf2);
						long long llval = va_arg(ap, long long);
						nchars_printed += printf(xf2, llval);
					}
				}
				free(xfmt);
				free(xf2);
			}
		}
	}
}

int main()
{
	int nc = 0;
	printf("orig: %x\n", 4534514);
	minprintf("mprf: %x\n", 4534514);
	printf("orig: %X\n", 4534514);
	minprintf("mprf: %X\n", 4534514);
	printf("orig: %E\n", 4.6);
	minprintf("mprf: %E\n", 4.6);
	printf("orig: %G\n", 4.6);
	minprintf("mprf: %G\n", 4.6);
	printf("orig: %a\n", -4.6);
	minprintf("mprf: %a\n", -4.6);
	printf("orig: %A\n", -4.6);
	minprintf("mprf: %A\n", -4.6);
	printf("orig: %p\n", &nc);
	minprintf("mprf: %p\n", &nc);
	printf("orig: %ld\n", 50420402L);
	minprintf("mprf: %ld\n", 50420402L);
	char tstr[50] = "foobar";
	printf("orig: '%s' '%s'\n", tstr, tstr);
	minprintf("mprf: '%s' '%s'\n", tstr, tstr);
}

