#include <stdio.h>
#define lmax 10
#define tabsize 4

void detab(char x[])
{
	char y[tabsize];
	for(int i = 0; i < tabsize; i++)
	{
		y[i] = x[i];
		if(x[i] == '\0')
		{
			break;
		}
	}
	int ctr = 0;
	while(ctr < lmax - 1)
	{
	}
}

void xprintf(char a[])
{
	printf("=====\n");
	for(int i=0; i < lmax; i++)
	{
		char c = a[i];
		if(c == '\0')
		{
			break;
		}
		printf("%d : %c : %d\n",i,c,c);
	}
}
int main()
{
	char c[lmax] = "123\t\t\t4";
	xprintf(c);
	detab(c);
	xprintf(c);
	return 0;
}




// output


// output


// output
// '123	4'
// '123    '


// output
// '123			4'
// '123    '


// output
// '123			4'
// '123    '


// output
// '123			4'
// '123    '


// output
// =====
// 0 : 11 : 22 : 33 : 	4 : 	5 : 	6 : 4=====
// 0 : 11 : 22 : 33 :  4 :  5 :  6 :  


// output
// =====
// 0 : 1
// 1 : 2
// 2 : 3
// 3 : 	
// 4 : 	
// 5 : 	
// 6 : 4
// =====
// 0 : 1
// 1 : 2
// 2 : 3
// 3 :  
// 4 :  
// 5 :  
// 6 :  


// output
// =====
// 0 : 1
// 1 : 2
// 2 : 3
// 3 : 	
// 4 : 	
// 5 : 	
// 6 : 4
// =====
// 0 : 1
// 1 : 2
// 2 : 3
// 3 :  
// 4 :  
// 5 :  
// 6 :  


// output
// =====
// 0 : 1 : 49
// 1 : 2 : 50
// 2 : 3 : 51
// 3 : 	 : 9
// 4 : 	 : 9
// 5 : 	 : 9
// 6 : 4 : 52
// =====
// 0 : 1 : 49
// 1 : 2 : 50
// 2 : 3 : 51
// 3 :   : 32
// 4 :   : 32
// 5 :   : 32
// 6 :   : 32


// output
// =====
// 0 : 1 : 49
// 1 : 2 : 50
// 2 : 3 : 51
// 3 : 	 : 9
// 4 : 	 : 9
// 5 : 	 : 9
// 6 : 4 : 52
// =====
// 0 : 1 : 49
// 1 : 2 : 50
// 2 : 3 : 51
// 3 :   : 32
// 4 :   : 32
// 5 :   : 32
// 6 :   : 32
