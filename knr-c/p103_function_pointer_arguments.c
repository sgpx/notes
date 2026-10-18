#include <stdio.h>

int return_five(void){
	return 5;
}

int sum(int a, int b){
	return (a+b);
}

int sum_ptr(int *a, int *b){
	return (*a) + (*b);
}

int times_two(int *x){
	return (*x)*2;
}

int exec(int (*f)(int*), int * x){
	return f(x);
}

int main(){
	// pointer to function with no arguments
	int (*c_return_five)() = return_five;
	printf("%d\n", c_return_five());

	// pointer to function with two int arguments
	int (*c_sum)(int,int) = sum;
	printf("%d\n", c_sum(7,5));

	// pointer to function with two int pointer arguments
	int (*c_sum_ptr)(int*,int*) = sum_ptr;
	int x1 = 8, x2 = 9;
	int *px1 = &x1, *px2 = &x2;
	printf("%d\n", c_sum_ptr(px1, px2));

	// pointer to function with an int pointer and a function pointer argument
	// cast
	int (*c_times_two)(int*) = times_two;
	int x3 = 21, *px3 = &x3;
	int (*c_exec)(int (*)(int*), int*) = exec;	
	printf("%d\n", c_exec(c_times_two, px3));

}
