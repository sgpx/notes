#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "h01_node.h"

nodeptr node_init(){
	nodeptr n = malloc(sizeof(node));
	n->next = NULL;
	n->name = NULL;
	n->defn = NULL;
	return n;
}

void install(char *name, char *defn){
	if(rptr == NULL)
		rptr = root;
	printf("installing %s : %s @ [%p]\n", name, defn, rptr);

	rptr->name = name;
	rptr->defn = defn;

	nodeptr next_node_ptr = node_init();
	rptr->next = next_node_ptr;
	rptr = rptr->next;
}

int check_node(nodeptr n, char *name){
	return strcmp(n->name, name) == 0;
}

void undef(char *name){
	printf("undef :: rptr : %p\n", rptr);
	rptr = root;
	nodeptr prev = NULL;

	while(rptr != NULL){
		if(rptr->name == NULL) break;
		if(check_node(rptr, name)) {
			printf("erasing %s @ %p\n", rptr->name, rptr);
			// first node

				// first node, nonsingle node

				// first node, single node

			// non-first node

				// non-last node

				// last node
			if(prev == NULL){ // first node
				if(rptr->next == NULL) { // first node, single node
					rptr->name = NULL;
					rptr->defn = NULL;
					rptr->next = NULL;
					return;
				}
				else { // first node, nonsingle node
					/*
					base @ b1:
						name: a1
						next: p1

					node1 @ p1:
						name: a2
						next: p2

					node2 @ p2:
						name: a3
						next: p3

					------------

					base @ b1:
						name: a1
						next: p2

					node2 @ p2:
						name: a3
						next: p3
					*/
					nodeptr tmp = rptr->next;
					rptr->name = tmp->name;
					rptr->defn = tmp->defn;
					rptr->next = tmp->next;
					free(tmp);
				}
			}
			else { // non-first node
				nodeptr tmp = rptr->next;
				rptr->name = tmp->name;
				rptr->defn = tmp->defn;
				rptr->next = tmp->next;
				free(tmp);
			}
		}
		prev = rptr;
		rptr = rptr->next;
	}
}

void freetree(){
	rptr = root->next;
	while(1){
		nodeptr tmp = rptr;
		printf("free : %p\n", tmp);

		if(rptr->next) {
			rptr = rptr->next;
			free(tmp);
		}
		else {
			free(tmp);
			break;
		}
	}
}

void print_tree(){
	for(rptr = root; rptr != NULL && rptr->name != NULL; rptr = rptr->next)
		printf("print : %p %s\n", rptr, rptr->name);
}




void test1()
{
	install("a1", "a1");
	install("a2", "a2");
	install("a3", "a3");
	print_tree();
	undef("a1");
	undef("a2");
	undef("a3");
	install("a4", "a4");
	print_tree();
	freetree();
}

void test2(){
	install("a1", "a1");
	undef("a1");
	//freetree();
}

void test3(){
	install("a1", "a1");
	install("a3", "a3");
	print_tree();
	undef("a3");
	print_tree();
	freetree();
}

void testZ(){
	install("a1", "a1");
	undef("a1");
	print_tree();
}
//void testN(){}

void testrun(){
	testZ();
}

int main(){
	testrun();
	return 0;
}

