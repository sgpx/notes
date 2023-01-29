#include <stdio.h>
#include <stdlib.h>

struct snode {
	int num;
	struct snode* next;
};

typedef struct snode node;


int main(){
	node* base = malloc(sizeof(node));
	base->num = 0;
	base->next = NULL;
	node* p = base;
	for(int i = 101; i < 110; i++){
		p->num = i;
		p->next = malloc(sizeof(node));
		p = p->next;
	}
	p = base;
	while(p != NULL){
		printf("%d\n", p->num);
		p = p->next;
	}
}
