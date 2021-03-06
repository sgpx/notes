#include <stdio.h>

void squeeze(char s[], char x)
{
	int i = 0;
	int j = 0;
	while(s[i] != '\0')
	{
		//printf("s[%d] %c s[%d] %c %s \n",i,s[i],j,s[j], s );

		s[j] = s[i];
		if(s[i] != x)
		{
			++j;
		}
		++i;
	}
	s[j] = '\0';
}

int main()
{
//	char foo[5] = "ababb";
	char foo[1024] = "abxyyaazzzzzaaa";
	printf("foo is %s\n",foo);
	squeeze(foo,'z');
	printf("foo is %s\n",foo);
	return 0;
}


// output
// bbbbb


// output
// bbbbb


// output


// output


// output


// output


// output
// foo is 


// output
// 0 0
// 1 0
// 2 0
// 3 0
// 4 0
// foo is 


// output
// 0 0
// 1 0
// 2 1
// 3 1
// 4 2
// foo is aba


// output
// ctr: 0 a, ctx: 0 a
// ctr: 1 b, ctx: 0 a
// ctr: 2 a, ctx: 0 a
// ctr: 3 b, ctx: 0 a
// ctr: 4 b, ctx: 0 a
// ctr: 5  , ctx: 0 a
// ctr: 6  , ctx: 0 a
// ctr: 7  , ctx: 0 a
// ctr: 8  , ctx: 0 a
// ctr: 9  , ctx: 0 a
// ctr: 10  , ctx: 0 a
// ctr: 11  , ctx: 0 a


// output
// ctr: 0 a, ctx: 0 a
// ctr: 1 b, ctx: 0 a
// ctr: 2 a, ctx: 0 a
// ctr: 3 b, ctx: 0 a
// ctr: 4 b, ctx: 0 a
// foo is ababb


// output
// ctr: 0 a, ctx: 0 a
// ctr: 1 b, ctx: 1 b
// ctr: 2 a, ctx: 1 a
// ctr: 3 b, ctx: 2 b
// ctr: 4 b, ctx: 3 b
// foo is ababb


// output
// foo is bbbbb


// output
// i 0 a
// j 0 a
// i 1 b
// j 0 a
// i 2 a
// j 1 b
// i 3 b
// j 1 a
// i 4 b
// j 2 a
// foo is bbbbb


// output
// s[0] a s[0] a 
// s[1] b s[0] a 
// s[2] a s[1] b 
// s[3] b s[1] a 
// s[4] b s[2] a 
// foo is bbbbb


// output
// s[0] a s[0] a ababb 
// s[1] b s[0] a ababb 
// s[2] a s[1] b bbabb 
// s[3] b s[1] a baabb 
// s[4] b s[2] a bbabb 
// foo is bbbbb


// output
// s[0] a s[0] a ababb 
// s[1] b s[0] a ababb 
// s[2] a s[1] b bbabb 
// s[3] b s[1] a baabb 
// s[4] b s[2] a bbabb 
// foo is bbbb


// output
// s[0] a s[0] a ababb 
// s[1] b s[0] a ababb 
// s[2] a s[1] b bbabb 
// s[3] b s[1] a baabb 
// s[4] b s[2] a bbabb 
// foo is bbb


// output
// s[0] a s[0] a abb 
// s[1] b s[0] a abb 
// s[2] b s[1] b bbb 
// foo is bb


// output
// s[0] a s[0] a abzsd 
// s[1] b s[1] b abzsd 
// s[2] z s[2] z abzsd 
// s[3] s s[2] z abzsd 
// s[4] d s[3] s abssd 
// foo is absd


// output
// foo is abzsdfsdaslawlelkzvxcvxcvxzwbs[0] a s[0] a abzsdfsdaslawlelkzvxcvxcvxzwb 
// s[1] b s[1] b abzsdfsdaslawlelkzvxcvxcvxzwb 
// s[2] z s[2] z abzsdfsdaslawlelkzvxcvxcvxzwb 
// s[3] s s[2] z abzsdfsdaslawlelkzvxcvxcvxzwb 
// s[4] d s[3] s abssdfsdaslawlelkzvxcvxcvxzwb 
// s[5] f s[4] d absddfsdaslawlelkzvxcvxcvxzwb 
// s[6] s s[5] f absdffsdaslawlelkzvxcvxcvxzwb 
// s[7] d s[6] s absdfssdaslawlelkzvxcvxcvxzwb 
// s[8] a s[7] d absdfsddaslawlelkzvxcvxcvxzwb 
// s[9] s s[8] a absdfsdaaslawlelkzvxcvxcvxzwb 
// s[10] l s[9] s absdfsdasslawlelkzvxcvxcvxzwb 
// s[11] a s[10] l absdfsdasllawlelkzvxcvxcvxzwb 
// s[12] w s[11] a absdfsdaslaawlelkzvxcvxcvxzwb 
// s[13] l s[12] w absdfsdaslawwlelkzvxcvxcvxzwb 
// s[14] e s[13] l absdfsdaslawllelkzvxcvxcvxzwb 
// s[15] l s[14] e absdfsdaslawleelkzvxcvxcvxzwb 
// s[16] k s[15] l absdfsdaslawlellkzvxcvxcvxzwb 
// s[17] z s[16] k absdfsdaslawlelkkzvxcvxcvxzwb 
// s[18] v s[16] z absdfsdaslawlelkzzvxcvxcvxzwb 
// s[19] x s[17] z absdfsdaslawlelkvzvxcvxcvxzwb 
// s[20] c s[18] v absdfsdaslawlelkvxvxcvxcvxzwb 
// s[21] v s[19] x absdfsdaslawlelkvxcxcvxcvxzwb 
// s[22] x s[20] c absdfsdaslawlelkvxcvcvxcvxzwb 
// s[23] c s[21] v absdfsdaslawlelkvxcvxvxcvxzwb 
// s[24] v s[22] x absdfsdaslawlelkvxcvxcxcvxzwb 
// s[25] x s[23] c absdfsdaslawlelkvxcvxcvcvxzwb 
// s[26] z s[24] v absdfsdaslawlelkvxcvxcvxvxzwb 
// s[27] w s[24] z absdfsdaslawlelkvxcvxcvxzxzwb 
// s[28] b s[25] x absdfsdaslawlelkvxcvxcvxwxzwb 
// foo is absdfsdaslawlelkvxcvxcvxwb


// output
// foo is abzsdfsdaslawlelkzvxcvxcvxzwb
// s[0] a s[0] a abzsdfsdaslawlelkzvxcvxcvxzwb 
// s[1] b s[1] b abzsdfsdaslawlelkzvxcvxcvxzwb 
// s[2] z s[2] z abzsdfsdaslawlelkzvxcvxcvxzwb 
// s[3] s s[2] z abzsdfsdaslawlelkzvxcvxcvxzwb 
// s[4] d s[3] s abssdfsdaslawlelkzvxcvxcvxzwb 
// s[5] f s[4] d absddfsdaslawlelkzvxcvxcvxzwb 
// s[6] s s[5] f absdffsdaslawlelkzvxcvxcvxzwb 
// s[7] d s[6] s absdfssdaslawlelkzvxcvxcvxzwb 
// s[8] a s[7] d absdfsddaslawlelkzvxcvxcvxzwb 
// s[9] s s[8] a absdfsdaaslawlelkzvxcvxcvxzwb 
// s[10] l s[9] s absdfsdasslawlelkzvxcvxcvxzwb 
// s[11] a s[10] l absdfsdasllawlelkzvxcvxcvxzwb 
// s[12] w s[11] a absdfsdaslaawlelkzvxcvxcvxzwb 
// s[13] l s[12] w absdfsdaslawwlelkzvxcvxcvxzwb 
// s[14] e s[13] l absdfsdaslawllelkzvxcvxcvxzwb 
// s[15] l s[14] e absdfsdaslawleelkzvxcvxcvxzwb 
// s[16] k s[15] l absdfsdaslawlellkzvxcvxcvxzwb 
// s[17] z s[16] k absdfsdaslawlelkkzvxcvxcvxzwb 
// s[18] v s[16] z absdfsdaslawlelkzzvxcvxcvxzwb 
// s[19] x s[17] z absdfsdaslawlelkvzvxcvxcvxzwb 
// s[20] c s[18] v absdfsdaslawlelkvxvxcvxcvxzwb 
// s[21] v s[19] x absdfsdaslawlelkvxcxcvxcvxzwb 
// s[22] x s[20] c absdfsdaslawlelkvxcvcvxcvxzwb 
// s[23] c s[21] v absdfsdaslawlelkvxcvxvxcvxzwb 
// s[24] v s[22] x absdfsdaslawlelkvxcvxcxcvxzwb 
// s[25] x s[23] c absdfsdaslawlelkvxcvxcvcvxzwb 
// s[26] z s[24] v absdfsdaslawlelkvxcvxcvxvxzwb 
// s[27] w s[24] z absdfsdaslawlelkvxcvxcvxzxzwb 
// s[28] b s[25] x absdfsdaslawlelkvxcvxcvxwxzwb 
// foo is absdfsdaslawlelkvxcvxcvxwb


// output
// foo is abzsdfsdaslawlelkzvxcvxcvxzwb
// foo is absdfsdaslawlelkvxcvxcvxwb


// output
// foo is abxyyaazzzzzaaa
// foo is abxyyaaaaa
