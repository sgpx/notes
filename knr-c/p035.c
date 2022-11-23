#include <stdio.h>
#define csize 100

// eliminate trailing whitespaces

int xgetline(char x[])
{
	//printf("enter line: \n");
	int ctr = 0;
	char c = getchar();
	int nonempty = 0;
	int last_nonempty_character = -1;
	while(c != '\n')
	{
		if(c != ' ' && c != '\t')
		{
			last_nonempty_character = ctr;
			nonempty = 1;
		}
		x[ctr] = c;
		++ctr;
		c = getchar();
	}
	if(nonempty == 0)
	{
		return -1;
	}
	if(last_nonempty_character < ctr)
	{
		x[last_nonempty_character+1] = '\0';
		return last_nonempty_character;
	}
	else
	{
		x[ctr] = '\0';
		return ctr;

	}
}

copy(char a[], char b[])
{
	int ctr = 0;
	char c = a[ctr];
	while( c != '\0' && ctr < csize)
	{
		c = a[ctr];
		b[ctr] = c;
		++ctr;
	}
}

main()
{
	char cl[csize];
	char ll[csize];

	int i = 0;
	int clen;
	int maxlen = 0;
	while(i < 2)
	{
		clen = xgetline(cl);
		if(clen == -1) // empty line
		{
			continue;
		}
		if(clen > maxlen)
		{
			maxlen = clen;
			copy(cl,ll);
		}
		if(clen > 5)
		{
			printf("line %d: '%s' \nlength: %d \n",i,cl,clen);
		}
		++i;
	}
	printf("longest line: %s\n",ll);
}




// output


// output


// output


// output


// output
// enter line: 
// line 0
// enter line: 
// line 1
// enter line: 
// line 2
// enter line: 
// line 3
// enter line: 
// line 4
// enter line: 
// line 5
// enter line: 
// line 6
// enter line: 
// line 7
// enter line: 
// line 8
// enter line: 
// line 9
// longest line: dfdwfrwnfwkarfn


// output
// enter line: 
// line 0: blah blah 
// length: 9 
// enter line: 
// line 1: bla 
// length: 3 
// enter line: 
// line 2: bl 
// length: 2 
// enter line: 
// line 3: bbbbb 
// length: 5 
// enter line: 
// line 4: hey 
// length: 3 
// enter line: 
// line 5: eeyy 
// length: 4 
// enter line: 
// line 6: aass 
// length: 4 
// enter line: 
// line 7: zzssss 
// length: 6 
// enter line: 
// line 8: meeeeeq 
// length: 7 
// enter line: 
// line 9: aas 
// length: 3 
// longest line: blah blah


// output
// line 0: abbb 
// length: 4 
// line 1: ds 
// length: 2 
// line 2: sd 
// length: 2 
// line 3: sd 
// length: 2 
// line 4: sd 
// length: 2 
// line 5: sd 
// length: 2 
// line 6: abbbbbbbbb 
// length: 10 
// line 7: xaaaaaaaaaaaa 
// length: 13 
// line 8: sdfsd 
// length: 5 
// line 9: adsdsww 
// length: 7 
// longest line: xaaaaaaaaaaaa


// output
// line 6: xxxxxxxxxxxxx 
// length: 13 
// longest line: xxxxxxxxxxxxx


// output
// line 0: aaaaa 
// length: 21 
// line 1: dfdsf 
// length: 20 
// line 2: df aaa 
// length: 6 
// line 3: ds a      ss 
// length: 12 
// line 4: sd     a 
// length: 8 
// line 5: df d                     dfd 
// length: 39 
// line 6: dfd                      fdf 
// length: 28 
// line 7: dfd                          dfdf 
// length: 50 
// line 8: dfd                          dfd                   dfd 
// length: 54 
// line 9: dfd                         dfd 
// length: 43 
// longest line: dfd                          dfd                   dfd


// output
// line 0: a     a 
// length: 12 
// line 1: abcde 
// length: 11 
// line 2: abcde 
// length: 12 
// line 3: abcde 
// length: 13 
// longest line: abcde


// output


// output
// line 1: 'abcdeeeeee' 
// length: 9 
// longest line: abcdeeeeee
