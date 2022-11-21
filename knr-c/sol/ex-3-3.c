#include <stdio.h>
#define CHARTYPE_ALPHA 1
#define CHARTYPE_NUM 2
#define CHARTYPE_OTHER 3

int chartype(char x)
{
	if (x >= 'a' && x <= 'z')
		return CHARTYPE_ALPHA;
	else if (x >= 'A' && x <= 'Z')
		return CHARTYPE_ALPHA;
	else if (x >= '0' && x <= '9')
		return CHARTYPE_NUM;
	else
		return CHARTYPE_OTHER;
}

void expand(char s[], char t[])
{
	int cts = 0, ctt = 0;
	while (s[cts] != '\0')
	{
		printf("cts: %d, ctt: %d\n", cts, ctt);
		if (s[cts] == '-')
		{
			char ls = s[cts - 1];
			char le = s[cts + 1];
			if (ls < le && chartype(ls) == chartype(le))
			{
				char z = ls + 1;
				while (z <= le)
				{
					t[ctt] = z;
					++ctt;
					++z;
				}
				cts += 2;
			}
			else
			{
				t[ctt] = s[cts];
				++cts;
				++ctt;
			}
		}
		else
		{
			t[ctt] = s[cts];
			++cts;
			++ctt;
		}
	}
	t[ctt] = '\0';
}

int main()
{
	char s[100] = "ba-z123xb-kA-Zxllx";
	char t[100];
	expand(s, t);
	printf("s: %s\n", s);
	printf("t: %s\n", t);
}
