#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int a;
} ta;
typedef ta *tptr;

int main() {
  ta e1;
  e1.a = 456;
  tptr e2 = &e1;
  printf("%d\n", e2->a);

  return 0;
}
