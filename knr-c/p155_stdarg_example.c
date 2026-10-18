#include <stdio.h>
#include <stdarg.h>

void fxn(int nargs, ...){
	va_list ap;
	va_start(ap, nargs);
	for(int i = 0; i < nargs; i++)
		printf("arg %d : %d\n", i, va_arg(ap, int));
}

int main(){
	fxn(2, 5, 6);
	return 0;
}
