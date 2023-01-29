/*
to remove last node

1. node * a = base
2. while(a->next != NULL) a = a->next;

=====

to remove first node
1. node * a = base
2. *a = *(a->next)

[0x01]
val : 25
next : 0x02

[0x02]
val : 26
next : 0x03

[0x03]
val : 27
next : NULL

----

[0x01]
val : 25
next : 0x03


*/

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

void print_for_ll(node *ref){
	node *p = ref;//, *q = ref;
	printf("rnll p : %p\n", p);
	for(node *p = ref; p != NULL; p = p->next){
		printf("rnll %p %d\n",p, p->num);
	}
}

void remove_node(node *ref, int x){
	node *p = ref;
	node *q = p->next;
	if(p == NULL) return;
	if(p->num == x){
		if(p->next != NULL){
			*p = *(p->next);
		}
	}
	// last element check
	else if(q != NULL && q->next == NULL && q->num == x){
		free(p->next);
		p->next = NULL;
		return;
	}
	else {
		p = p->next;
		remove_node(p, x);
	}
}

int main(){
	node base;
	assign_ll(&base);
	printf("before\n");
	print_ll(&base);
	remove_node(&base, 109);
	printf("after\n");
	print_ll(&base);
	free_ll(&base);
}

