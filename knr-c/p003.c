// print the celsius fahrenheit table
// 0 deg C = 32 deg F
// 100 deg C = 212 deg F
// 100 del C = 180 del F
// 1 del C = 180/100 del F
// temp_C / 100	= temp_F - 32 / 180
#include <stdio.h>

main() {
  int f, c;
  int u, step;

  f = 0;
  u = 400;
  step = 32;

  while (f <= u) {
    c = 5 * (f - 32) / 9;
    printf("Celsius %d C <=> Fahrenheit %d F\n", c, f);
    f = f + step;
  }
}
