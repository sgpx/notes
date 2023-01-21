#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#define KEY_SIZE 256 // bits
#define BLOCK_SIZE 128 // bits

#define DEBUG_MODE 0



typedef unsigned short ust;

unsigned short start_key_bits[KEY_SIZE];


int to_dec(unsigned short tmp[]){
        int val = 0;
        for(int i = 0; i < 4; i++){
		if(DEBUG_MODE) printf("%d\n", tmp[i]);
                int digit = tmp[i];
                int pv = digit * pow(2, 4-i-1);
                val += pv;
        }
	if(DEBUG_MODE) printf("val : %d\n", val);
        return val;
}

int random_number(){
	int r = rand() % 2;
	return r;
}

void initialize_random_seed(){
	srand(time(NULL));
}

void generate_start_key_bits(){
	for(int i = 0; i < KEY_SIZE; i++)
		start_key_bits[i] = random_number();

	if(DEBUG_MODE)
		for(int i = 0; i < KEY_SIZE; i++)
				printf("%d", start_key_bits[i]);
	if(DEBUG_MODE)
			printf("\n");

}

char bin_to_hex_byte(int x){
	int base = 16;
	if(x <= 9) return '0' + x;
	else return 'A' + x - 10;
}



void bin_to_hex(ust start_key_bits[], char out[]) {
	int ctr = 0, hbctr = 0;
	while(ctr < KEY_SIZE){
		ust tmp[4];
		for(int i = 0; i < 4; i++){
			tmp[i] = start_key_bits[ctr + i];
		}
		int res = to_dec(tmp);
		char a = bin_to_hex_byte(res);
		if(DEBUG_MODE) printf("res: %d, a: %c\n", res, a);
		out[hbctr++] = a;
		ctr += 4;
	}
	out[hbctr] = '\0';
	if(DEBUG_MODE) printf("\n");
}

int main() {
	initialize_random_seed();
	generate_start_key_bits();
	char res[100];
	bin_to_hex(start_key_bits, res);
	printf("%s\n", res);
}
