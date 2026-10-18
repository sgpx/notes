#include <stdio.h>
#include <stdlib.h>

struct node_struct {
	int num;
	struct node_struct *next;
};

typedef struct node_struct node;

void assign_ll(node *ref){
	node *p = ref;
	for(int i = 101; i < 110; i++){
		p->num = i;
		p->next = malloc(sizeof(node));
		p = p->next;
	}
	// avoid valgrind uninitialized errors
	p->num = 110;
	p->next = NULL;
}

void print_ll(node *ref){
	node *p = ref;
	while(p != NULL){
		printf("%p %d\n", p, p->num);
		p = p->next;
	}
}

void free_ll(node *ref){
	node *p = ref, *q;
	p = p->next;
	while(p != NULL){
		q = p;
		p = p->next;
		free(q);
	}
}

int main(){
	node base;
	assign_ll(&base);
	print_ll(&base);
	free_ll(&base);
}

