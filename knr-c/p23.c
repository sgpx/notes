#include <stdio.h>

main()
{
	int number_of_lines, number_of_words, number_of_characters;
	number_of_lines = 0;
	number_of_words = 0;
	number_of_characters = 0;

	int state; 
	state = 0;

	char c = getchar();
	while(c != EOF)
	{
		number_of_characters++;
		if( c == '\n'){ ++number_of_lines ; }
		if ( c == '\n' || c == ' ' || c == '\t'){ state = !state; }
		else if ( state == 1 ){ ++number_of_words; }
		c = getchar();
	}

	printf("%d \n", number_of_lines);
	printf("%d \n", number_of_words);
	printf("%d \n", number_of_characters);

}


// output


// output


// output


// output


// output


// output
// 2 
// 23 
// 59 


// output
// 1 
// 5 
// 25 
