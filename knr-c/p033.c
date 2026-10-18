#include <stdio.h>
#define csize 100


int xgetline(char x[])
{
	//printf("enter line: \n");
	int ctr = 0;
	char c = getchar();
	while(c != '\n')
	{
		x[ctr] = c;
		++ctr;
		c = getchar();
	}
	x[ctr] = '\0';
	return ctr;
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
	while(i < 10)
	{
		clen = xgetline(cl);
		if(clen > maxlen)
		{
			maxlen = clen;
			copy(cl,ll);
		}
		printf("line %d: %s \nlength: %d \n",i,cl,clen);
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
