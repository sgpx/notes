#include <stdio.h>

void squeeze(char s[], char x)
{
	int i = 0;
	int j = 0;
	while(s[i] != '\0')
	{
		printf("s[%d] %c s[%d] %c %s \n",i,s[i],j,s[j], s );

		s[j] = s[i];
		if(s[i] != x)
		{
			++j;
		}
		++i;
	}
	s[j] = '\0';
}

void string_squeeze(char foo[], char bar[])
{
	printf("bar is %s\n",bar);
	int i = 0;
	while(bar[i] != '\0')
	{
		printf("target is %c %d\n",bar[i],bar[i]);
		/*printf("foo is %s\n",foo);
		char target_char = bar[i];
		squeeze(foo,target_char);
		printf("foo is %s\n",foo);
		printf("===\n");*/
		++i;
	}
}

int main()
{
	char a[5] = "blah";
 	char b[3] = "ah";
	string_squeeze(a,b);
	printf("a is %s\n",a);
}

// output
// foo is abxyyaazzzzzaaa
// foo is bxyyzzzzz
// foo is bxyyzzzzz
// foo is xyyzzzzz
// foo is xyyzzzzz
// foo is yyzzzzz


// output


// output


// output
// bar is ahblahbfoo is blahb
// foo is blhb
// foo is blhb
// foo is blb
// foo is blb
// foo is l
// l


// output
// bar is ahblahb
// foo is blahb
// foo is blhb
// foo is blhb
// foo is blb
// foo is blb
// foo is l
// l


// output
// bar is ahblahb
// foo is blahb
// foo is blhb
// foo is blhb
// foo is blb
// foo is blb
// foo is l
// a is l


// output
// bar is ahblahb
// foo is blahb
// s[0] b s[0] b blahb 
// s[1] l s[1] l blahb 
// s[2] a s[2] a blahb 
// s[3] h s[2] a blahb 
// s[4] b s[3] h blhhb 
// foo is blhb
// foo is blhb
// s[0] b s[0] b blhb 
// s[1] l s[1] l blhb 
// s[2] h s[2] h blhb 
// s[3] b s[2] h blhb 
// foo is blb
// foo is blb
// s[0] b s[0] b blb 
// s[1] l s[0] b blb 
// s[2] b s[1] l llb 
// foo is l
// a is l


// output
// bar is ahblahb
// foo is blahb
// s[0] b s[0] b blahb 
// s[1] l s[1] l blahb 
// s[2] a s[2] a blahb 
// s[3] h s[2] a blahb 
// s[4] b s[3] h blhhb 
// foo is blhb
// ===
// foo is blhb
// s[0] b s[0] b blhb 
// s[1] l s[1] l blhb 
// s[2] h s[2] h blhb 
// s[3] b s[2] h blhb 
// foo is blb
// ===
// foo is blb
// s[0] b s[0] b blb 
// s[1] l s[0] b blb 
// s[2] b s[1] l llb 
// foo is l
// ===
// a is l


// output
// bar is ahblah
// foo is blah
// s[0] b s[0] b blah 
// s[1] l s[1] l blah 
// s[2] a s[2] a blah 
// s[3] h s[2] a blah 
// foo is blh
// ===
// foo is blh
// s[0] b s[0] b blh 
// s[1] l s[1] l blh 
// s[2] h s[2] h blh 
// foo is bl
// ===
// foo is bl
// s[0] b s[0] b bl 
// s[1] l s[0] b bl 
// foo is l
// ===
// a is l


// output
// bar is ahblah
// target is a 97
// foo is blah
// s[0] b s[0] b blah 
// s[1] l s[1] l blah 
// s[2] a s[2] a blah 
// s[3] h s[2] a blah 
// foo is blh
// ===
// target is h 104
// foo is blh
// s[0] b s[0] b blh 
// s[1] l s[1] l blh 
// s[2] h s[2] h blh 
// foo is bl
// ===
// target is b 98
// foo is bl
// s[0] b s[0] b bl 
// s[1] l s[0] b bl 
// foo is l
// ===
// a is l


// output
// bar is ahblah
// target is a 97
// foo is blah
// s[0] b s[0] b blah 
// s[1] l s[1] l blah 
// s[2] a s[2] a blah 
// s[3] h s[2] a blah 
// foo is blh
// ===
// target is h 104
// foo is blh
// s[0] b s[0] b blh 
// s[1] l s[1] l blh 
// s[2] h s[2] h blh 
// foo is bl
// ===
// target is b 98
// foo is bl
// s[0] b s[0] b bl 
// s[1] l s[0] b bl 
// foo is l
// ===
// a is l


// output
// bar is ahblah
// target is a 97
// target is h 104
// target is b 98
// target is l 108
// target is a 97
// target is h 104
// a is blah


// output
// bar is ah
// target is a 97
// target is h 104
// a is blah
