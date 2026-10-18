#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define HASHSIZE 101
#define NUM_INPUT_LINES 100
#define MACRO_LEN 100

struct snode
{
  char *name;
  char *defn;
  struct snode *next;
};

typedef struct snode node;
typedef node *nodeptr;

node base[101];
nodeptr root = NULL;
nodeptr rptr = NULL;

unsigned hash(char *s) {
        unsigned hashval;
	printf("calculating hash for '%s'\n", s);
        for (hashval = 0; *s != '\0'; s++)
                hashval = *s + 31 * hashval;
	printf("hashval is %d\n", hashval % HASHSIZE);
        return (hashval % HASHSIZE);
}

int check_node(nodeptr n, char *name) {
	return strcmp(n->name, name) == 0;
}

void move_to_last_node(){
	while(rptr->next != NULL)
		rptr = rptr->next;
}

void set_root(char *name) {
	unsigned hashvalue = hash(name);
	printf("setting root = base[%d]\n", hashvalue);
	root = &base[hashvalue];
	rptr = root;
}

nodeptr node_init() {
	nodeptr n = malloc(sizeof(node));
	n->next = NULL;
	n->name = NULL;
	n->defn = NULL;
	return n;
}

nodeptr lookup(char *name){
	set_root(name);
	nodeptr res = NULL;

	for(rptr = root; rptr != NULL && rptr->name != NULL; rptr = rptr->next)
		if(check_node(rptr, name)) {
			res = rptr;
			break;
		}

	return res;
}

void install(char *name, char *defn) {
	set_root(name);
	nodeptr tmp = lookup(name);
	if(tmp != NULL) {
		printf("setting %s : %s after lookup\n", name, defn);
		(*tmp).defn = defn;
		return;
	}
	move_to_last_node(); // for installation
	printf("root is %p\n", root);
	printf("installing %s : %s @ [%p]\n", name, defn, rptr);

	rptr->name = name;
	rptr->defn = defn;

	nodeptr next_node_ptr = node_init();
	rptr->next = next_node_ptr;
	rptr = rptr->next;
}


void undef(char *name) {
	set_root(name);
	printf("undef :: rptr : %p\n", rptr);
	nodeptr prev = NULL;

	while(rptr != NULL) {
		if(rptr->name == NULL) break;
		if(check_node(rptr, name)) {
			printf("erasing %s @ %p\n", rptr->name, rptr);
			// first node

				// first node, nonsingle node

				// first node, single node

			// non-first node

				// non-last node

				// last node
			if(prev == NULL) { // first node
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


void freesub() {
	rptr = root->next;
	while(1) {
		if(rptr == NULL) break;

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

void freetree(){
	for(int i = 0; i < HASHSIZE; i++) {
		root = &base[i];
		freesub();
	}
}


void print_tree() {
	for(int i = 0; i < HASHSIZE; i++)
		for(rptr = &base[i]; rptr != NULL && rptr->name != NULL; rptr = rptr->next)
			printf("print :: sub %d [%p] :: %p %s\n", i, &base[i], rptr, rptr->name);
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

void test2() {
	install("a1", "a1");
	undef("a1");
	//freetree();
}

void test3() {
	install("a1", "a1");
	install("a3", "a3");
	print_tree();
	undef("a3");
	print_tree();
	freetree();
}

void test4() {
	install("a1", "a1");
	undef("a1");
	print_tree();
}

void test5() {
	install("a1", "a1");
	install("a2", "a1");
	install("a3", "a1");
	install("a4", "a1");
	undef("a4");
	undef("a1");
	print_tree();
}

void test6() {
	install("a1", "a1");
	install("a2", "a1");
	install("a3", "a1");
	install("a4", "a1");
	undef("a4");
	undef("a3");
	undef("a2");
	undef("a1");
	print_tree();
	freetree();
}

void test7() {
	install("a1", "a1");
	install("a2", "a1");
	install("a3", "a1");
	install("a4", "a1");
	print_tree();
	freetree();
}

char dpairlist[NUM_INPUT_LINES][2][MACRO_LEN];
int dpctr = 0;

void process_input(){
	printf("process_input\n");
	char *name = dpairlist[dpctr][0], *defn = dpairlist[dpctr][1];
	char cmd[10];
	do {
		scanf("%s", cmd);
		if(cmd[0] == EOF)
			break;
		else if(strcmp(cmd, "#define") == 0){
			scanf("%s %s", name, defn);
			install(name, defn);
		}
		else if(strcmp(cmd, "#undef") == 0){
			scanf("%s", name);
			undef(name);
		}
		else if(strcmp(cmd, "#printdef") == 0){
			scanf("%s", name);
			nodeptr res = lookup(name);
			printf("printdef %s : %s\n", name, res ? res->defn : "not found");
		}
		dpctr++;
	}
	while(cmd[0] != EOF);

}

void test8(){
	process_input();
}

void test9() {
	install("a1", "a1");
	install("a2", "a1");
	install("a3", "a1");
	install("a4", "a1");
	printf("lookup result : %p\n", lookup("a1"));
	printf("lookup result : %p\n", lookup("a5"));
}

void testZ() {
	install("a1", "a1");
	printf("\n\nlookup result : %s\n\n", lookup("a1")->defn);
	install("a1", "z");
	printf("\n\nlookup result : %s\n\n", lookup("a1")->defn);
}

//void testN() {}

void testrun() {
	test8();
}


int main() {
	testrun();
	return 0;
}

