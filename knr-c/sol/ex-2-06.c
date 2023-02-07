/*
ex 2-6
*/

#include <stdio.h>
#include <math.h>

int countbits(int x){
	int lx = 0;
	int tmp = x;
	while(tmp){
		tmp = tmp >> 1;
		++lx;
	}
	return lx;
}

void bitprintf(int a[], int l){
	for(int i = 0; i < l; i++)
	{
		printf("%d ", a[i]);
	}
	printf("\n");
}

void tobits(int a[], int l, int b){
	printf("val : %d\n", b);
	int ol = l;
	while(b){
		a[l-1] = b % 2;
		b = b >> 1;
		--l;
	}
	bitprintf(a, ol);
}

int todec(int a[], int l){
	int s = 0;
	for(int i = 0; i < l; i++){
		int exp = l - i - 1;
		s = s + (a[i] * pow(2, exp));	
	}
	return s;
}

int setbits(int x, int p, int n, int y){
	int lx = countbits(x);
	int ly = countbits(y);
	printf("p : %d, n : %d\n", p, n);
	printf("lx : %d, ly : %d\n", lx, ly);

	int arx[lx], ary[ly];

	tobits(arx, lx, x);
	tobits(ary, ly, y);

	int spx = p;
	int spy = ly - n;

	for(int i = 0; i < n; i++){
		printf("i : %d, spx+i : %d, spy+i : %d, arx[spx+i] : %d -> ary[spy+i] : %d\n", i, spx+i, spy+i, arx[spx+i], ary[spy+i]);
		arx[spx + i] = ary[spy + i];
	}
	printf("arx\n");
	bitprintf(arx, lx);

	return todec(arx, lx);
}

int main(){
	int a = setbits(25, 0, 2, 28);
	printf("a : %d\n", a);
}
