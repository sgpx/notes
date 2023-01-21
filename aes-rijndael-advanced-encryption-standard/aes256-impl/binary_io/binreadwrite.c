#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define DEBUG_MODE_1 1
#define DEBUG_MODE_2 1


unsigned short xchar_bits[8];


void to_bits(int x){
	if(DEBUG_MODE_2)
		printf("to_bits x : %d\n", x);

	unsigned short tmp[8];
	for(int u = 0; u < 8; u++) tmp[u] = 0;
	int a = x, ctr = 0;
	while(ctr < 8){
		if(a > 0) {
			int rem = a % 2;
			tmp[ctr++] = rem;
			a -= rem;
			a /= 2;
		}
		else
			tmp[ctr++] = 0;
	}

	for(int j = 0; j < 8; j++)
		xchar_bits[j] = tmp[8 - j - 1];

	if(DEBUG_MODE_2)
		for(int j = 0; j < 8; j++)
			printf("%d", xchar_bits[j]);

	if(DEBUG_MODE_2) printf("\n");
}

int to_bin(unsigned short tmp[]){
	int val = 0;
	for(int i = 0; i < 8; i++){
		int digit = tmp[i];
		if(DEBUG_MODE_2) printf("%d", digit);
		int pv = digit * pow(2,8-i-1);
		val += pv;
	}
	if(DEBUG_MODE_2) printf("\n");
	return val;
}

void binwrite(unsigned short * sbuf, unsigned short * sptr){
	unsigned short *q = sbuf;
	FILE *wrf = fopen("z.out", "wb");
	while(q < sptr){
		unsigned short tmp[8];
		for(int i=0; i<8; i++){
			tmp[i] = *(q+i);
		}
		int bw = to_bin(tmp);
		fputc(bw, wrf);
		q += 8;
	}
	fclose(wrf);
}

int main(int argc, char **argv){
	if(argc < 2) return 1;
	char *fn = argv[1];
	FILE *fp;
	fp = fopen(fn, "rb");
	unsigned int fctr = 0;
	while(fgetc(fp) != EOF) fctr++;
	fclose(fp);
	unsigned int effsizebits = fctr * sizeof(unsigned char)*8;
	if(DEBUG_MODE_1) printf("effsizebits : %d\n", effsizebits);


	unsigned short *sbuf = (unsigned short*)malloc(effsizebits * 8);
	unsigned short *sptr = sbuf;
	fp = fopen(fn, "rb");
	int c;
	size_t sz = 1; //sizeof(unsigned short);
	while( (c=fgetc(fp)) != EOF ){
		to_bits(c);
		if(DEBUG_MODE_1) printf("%p %ld %d\n", sptr, sptr-sbuf, effsizebits);
		for(int u = 0; u < 8; u++){
			*sptr = xchar_bits[u];
			if(DEBUG_MODE_2) printf("sptr : %p, *sptr : %d, dif : %ld\n", sptr, *sptr, sptr-sbuf);
			sptr += 1;
		}
	}

	if(DEBUG_MODE_2)
		for(unsigned short *q = sbuf; q != sptr; q += sz)
			printf("%p : %d\n", q, *q);

	binwrite(sbuf, sptr);
}
