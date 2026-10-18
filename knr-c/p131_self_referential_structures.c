#include <stdio.h>

 struct tnode {
	char *word;
	int count;
	struct tnode *left;
	struct tnode *right;
};

typedef struct tnode tnd;

int main(){
    tnd a;
    a.word = "lol";
    a.count = 0;
    tnd b;
    b.word = "lmao";
    b.count = 5;
    a.left = &b;
    printf("%s %s\n", a.word, a.left->word);

}