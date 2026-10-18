#include <stdio.h>
#include <stdarg.h>
int isfmtchar(char c)
{
	if (c == '.')
		return 1;
	else if (c == '+' || c == '-')
		return 1;
	else if (c >= '0' && c <= '9')
		return 1;
	else
		return 0;
}

void minscanf(char *fmt, ...)
{
	va_list ap;
	va_start(ap, fmt);
	char *p = fmt;
	while (*p != '\0')
	{
		char d;
		if (*p == '%')
		{
			++p;
			if (*p == '%')
			{
				d = getchar();
				if (d != *p)
					break;
			}
			else
			{
				char sfmt[20], *sptr = sfmt;
				*sptr++ = '%';
				if (isfmtchar(*p))
				{
					while (isfmtchar(*p))
					{
						*sptr = *p;
						++sptr;
						++p;
					}
				}
				*sptr++ = *p;
				*sptr = '\0';

				char dtype = *p;
				if (dtype == 'c')
				{
					char *cval = va_arg(ap, char *);
					scanf(sfmt, cval);
				}
				else if (dtype == 'd' || dtype == 'i' || dtype == 'o' || dtype == 'x')
				{
					int *ival = va_arg(ap, int *);
					scanf(sfmt, ival);
				}
				else if (dtype == 'f' || dtype == 'e' || dtype == 'g')
				{
					double *dval = va_arg(ap, double *);
					scanf(sfmt, dval);
				}
				else if (dtype == 's')
				{
					char *sval = va_arg(ap, char *);
					scanf(sfmt, sval);
				}
				else if (dtype == 'u')
				{
					unsigned *uval = va_arg(ap, unsigned *);
					scanf(sfmt, uval);
				}
				else if (dtype == 'l')
				{
					++p;
					while (*p == 'l')
						*(sptr++) = *(p++);
					*sptr++ = *p;
					*sptr = '\0';
					if (*p == 'd')
					{
						long long *lval = va_arg(ap, long long *);
						scanf(sfmt, lval);
					}
					else if (*p == 'u')
					{
						unsigned long long *ullval = va_arg(ap, unsigned long long *);
						scanf(sfmt, ullval);
					}
				}
				printf("sfmt : %s\n", sfmt);
			}
		}
		else
		{
			char d = getchar();
			if (d != *p)
				break;
		}
		++p;
	}
	return;
}

void realtestrun()
{
	int p1 = 0, p3 = 0, q1 = 0, q3 = 0;
	char p2[1024], q2[1024];
	printf("using scanf\n");
	scanf("%d_%s_%d", &p1, p2, &p3);
	printf("scanf: %d %s %d\n", p1, p2, p3);

	printf("using minscanf\n");
	minscanf("%d_%s_%d", &q1, p2, &q3);
	printf("minscanf: %d %s %d\n", q1, q2, q3);
}

void test1()
{
	int x = 0;
	minscanf("%d", &x);
	printf("%d", x);
}

void test2()
{
	int x = 0, y = 0;
	minscanf("%d_%d", &x, &y);
	printf("x : %d, y : %d", x, y);
}

void test3()
{
	int x = 0, y = 0;
	minscanf("%d_%d,", &x, &y);
	printf("x : %d, y : %d", x, y);
}

void test4()
{
	unsigned long long int x = 0;
	minscanf("%llu,", &x);
	printf("x : %llu", x);
}

void test5()
{
	long long int x = 0;
	minscanf("%lld,", &x);
	printf("x : %lld", x);
}

void test6()
{
	char a[10], b[10];
	minscanf("%s_%s", a, b);
	printf("a : %s, b : %s\n", a, b);
}

void test7()
{
	char a[10], b[10];
	minscanf("%c_%c", &a[0], &b[0]);
	printf("a : %c, b : %c\n", a[0], b[0]);
}

void test8()
{
	int a;
	char b;
	minscanf("%d_%c", &a, &b);
	printf("a : %d, b : %c\n", a, b);
}

void testrun(){
	test8();
}

int main()
{
	testrun();
	return 0;
}
