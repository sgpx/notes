struct snode
{
  char *name;
  char *defn;
  struct snode *next;
};

typedef struct snode node;
typedef node *nodeptr;

node base;
nodeptr root = &base;
nodeptr rptr = &base;
