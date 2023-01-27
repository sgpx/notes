#include <stdio.h>
typedef struct {
  int x;
} tt;

void f(tt *ptr) { printf("%d\n", ptr->x); }

int main() {
  tt a;
  a.x = 123;
  f(&a);
  return 0;
}
