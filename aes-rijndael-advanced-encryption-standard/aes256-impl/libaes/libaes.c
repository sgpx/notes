#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "rijndael_constants.h"

#define KEY_SIZE 256
#define ROUND_KEY_SIZE 128 // bits
#define BLOCK_SIZE 128
#define WORD_SIZE 32
#define NUM_WORDS KEY_SIZE / WORD_SIZE // 8
#define NUM_ROUND_KEYS_NEEDED 15

#define KEYFILE "key.txt"
#define IFN "rawdata.bin"
#define OFN "edata.bin"

typedef unsigned long long ull;
typedef unsigned char uch;

ull start_key_wordval[NUM_WORDS];
ull expanded_key_words[NUM_ROUND_KEYS_NEEDED * 4];

char *keybuf = NULL, *keyptr = NULL;
char *plaintextbuf = NULL, *plaintextptr = NULL;

ull round_key_val = 0;
uch round_key_bits[128];
uch round_key_word_ctr = 0;

void print_array(const char *msg, uch x[], int len)
{
	printf("%s\n", msg);
	for (int i = 0; i < len; i++)
		printf("%d, ", x[i]);
	printf("\n");
}

void to_bits(ull x, ull len, uch arr[])
{
	int i = 0;

	for (int u = 0; u < len; u++)
		arr[u] = 0;

	while (x)
	{
		int rem = x % 2;
		arr[len - i - 1] = rem;
		x -= rem;
		x /= 2;
		++i;
	}

	/*
	for (int i = 0; i < len; i++)
		printf("%d", arr[i]);
	printf("\n");
	*/
}

void read_key_from_file(void)
{
	FILE *fp = fopen(KEYFILE, "rb");
	char c;
	int ctr = 0;

	while (fgetc(fp) != EOF)
		++ctr;

	fseek(fp, 0L, SEEK_SET);
	keybuf = (char *)malloc(ctr * sizeof(char));
	keyptr = keybuf;

	while ((c = fgetc(fp)) != EOF && c != '\n')
	{
		*keyptr = c;
		++keyptr;
	}

	*keyptr = '\0';
	fclose(fp);
}

void read_plaintext_from_file(void)
{
	FILE *fp = fopen(IFN, "rb");
	char c;
	int ctr = 0;

	while (fgetc(fp) != EOF)
		++ctr;

	fseek(fp, 0L, SEEK_SET);
	plaintextbuf = (char *)malloc(ctr * sizeof(char));
	plaintextptr = plaintextbuf;

	while ((c = fgetc(fp)) != EOF && c != '\n')
	{
		*plaintextptr = c;
		++plaintextptr;
	}

	*plaintextptr = '\0';
	printf("plaintext : %s\n", plaintextbuf);
	fclose(fp);
}

void cleanup(void)
{
	free(keybuf);
	free(plaintextbuf);
}

char *get_keybuf(void)
{
	return keybuf;
}

int get_character_value(char c)
{
	if (c >= '0' && c <= '9')
		return c - '0';
	else if (c >= 'A' && c <= 'F')
		return 10 + c - 'A';
}

void char_to_4bits(char c, uch tmp[], uch ctr)
{
	int val = get_character_value(c);
	int a = val, i = ctr + 3;
	while (a > 0)
	{
		int rem = a % 2;
		// printf("i : %d, val : %d, a : %d, rem : %d\n", i, val, a, rem);

		tmp[i] = rem;
		a -= rem;
		a /= 2;
		--i;
	}
}

unsigned int to_decimal(uch arr[], int len)
{
	int val = 0;
	for (int i = 0; i < len; i++)
	{
		val += pow(2, len - 1 - i) * arr[i];
	}
	return val;
}

void split_key_to_32bit_words(void)
{
	int wordctr = 0;
	char *cptr = get_keybuf();
	uch wstor[NUM_WORDS][32];
	while (wordctr < NUM_WORDS)
	{
		printf("wordctr : %d, c : %c, value of c : %d\n", wordctr, *cptr, get_character_value(*cptr));
		uch *tmp = wstor[wordctr], tmpctr = 0;
		for (int i = 0; i < 32; i++)
			tmp[i] = 0;
		for (int i = 0; i < 8; i++)
		{
			char c = *cptr;
			printf("c : %c\n", c);
			++cptr;
			char_to_4bits(c, tmp, tmpctr);
			tmpctr += 4;
		}
		printf("word %d start\n", wordctr);
		for (int i = 0; i < 32; i++)
			printf("i : %d, tmp[i] : %d\n", i, tmp[i]);
		printf("word %d end\n", wordctr);
		wordctr += 1;
	}

	for (int i = 0; i < 8; i++)
	{
		start_key_wordval[i] = to_decimal(wstor[i], 32);
		printf("start_key_wordval of word %d  : %lld\n", i, start_key_wordval[i]);
	}
	// key is 256 bits
	// one char represents 4 bits
	// each 32 bit word needs 8 chars
}

void test_to_decimal(void)
{
	uch xarr[8] = {1, 0, 0, 0, 0, 0, 0, 1};
	printf("%d\n", to_decimal(xarr, 8));
}

ull sub_word(ull wx)
{
	uch arr[32], res[32];
	to_bits(wx, 32, arr);
	for (int i = 0; i < 4; i++)
	{
		uch msn[4], lsn[4];
		int msv = 0, lsv = 0;
		for (int j = 0; j < 8; j++)
		{
			if (j < 4)
			{
				msn[j] = arr[(8 * i) + j];
			}
			else
			{
				lsn[j - 4] = arr[(8 * i) + j];
			}
		}
		msv = to_decimal(msn, 4);
		lsv = to_decimal(lsn, 4);

		print_array("msn4", msn, 4);
		printf("msv : %d\n", msv);

		print_array("lsn4", lsn, 4);
		printf("lsv : %d\n", lsv);

		// row : msv
		// col : lsv

		int pc = (msv * 16) + lsv;
		printf("pc : %d\n", pc);

		uch subbyte = sbox[pc];
		printf("subbyte : %d\n", subbyte);
		uch subarr[8];
		to_bits(subbyte, 8, subarr);
		print_array("subarr", subarr, 8);

		for (int j = 0; j < 8; j++)
		{
			res[(8 * i) + j] = subarr[j];
		}
	}
	print_array("subword res", res, 32);
	ull rv = to_decimal(res, 32);
	return rv;
}

ull rot_word(ull wx)
{
	// word is 32 bits
	// word is 4 bytes
	// take first byte and move it to the end
	uch arr[32];
	// uch res[32];
	to_bits(wx, 32, arr);
	uch mv1[8], mv2[24];
	ull rsx = 0;

	for (int i = 0; i < 32; i++)
	{
		if (i < 8)
			mv1[i] = arr[i];
		else
		{
			mv2[i - 8] = arr[i];
		}
	}

	for (int i = 0; i < 32; i++)
	{
		if (i < 24)
		{
			rsx += pow(2, 32 - i - 1) * mv2[i];
		}
		else
		{
			rsx += pow(2, 32 - i - 1) * mv1[i - 24];
		}
	}
	return rsx;
}

ull get_rcon(ull x)
{
	return rcon_array[x];
}

void get_expanded_key_words(void)
{
	const int r = NUM_ROUND_KEYS_NEEDED;
	const int N = NUM_WORDS;
	ull w[NUM_ROUND_KEYS_NEEDED * 4];
	// 60x words of size 32bit of expanded key
	// each Wx word is 32bits
	// each round key Kx is 4 words = 128 bits
	// Kx1 = [Wx0, Wx1, Wx2, Wx3, ... Wx7]
	// 60*32 = 1920 bits
	// 1920/128 = 15 == number of rounds

	for (int i = 0; i < (4 * r); i++)
	{
		if (i < N)
		{
			w[i] = start_key_wordval[i];
		}
		else if (i >= N && i % N == 0)
		{
			w[i] = w[i - N] ^ sub_word(rot_word(w[i - 1])) ^ get_rcon(i / N);
		}
		else if (i >= N && N > 6 && i % N == 4)
		{
			w[i] = w[i - N] ^ sub_word(w[i - 1]);
		}
		else
		{
			w[i] = w[i - N] ^ w[i - 1];
		}
		printf("key : %d, val : %lld\n", i, w[i]);
		expanded_key_words[i] = w[i];
	}
}

void test_rot_word()
{
	ull q = 3647703299;
	ull ans = rot_word(q);
	printf("%lld\n", q);
	printf("%lld\n", ans);
}

void test_sub_word()
{
	ull q = 3647703299;
	ull ans = sub_word(q);
	printf("q : %lld\n", q);
	printf("a : %lld\n", ans);
}

void rk_get_next_128bits(uch a[])
{
	uch res[128], rc = 0;
	for (int i = round_key_word_ctr; i < round_key_word_ctr + 4; i++)
	{
		ull word = expanded_key_words[i];
		uch tmp[32];
		to_bits(word, 32, tmp);
		for (int j = 0; j < 32; j++)
			res[rc++] = tmp[j];
	}
	round_key_word_ctr += 4;
	for (int i = 0; i < 128; i++)
		a[i] = res[i];
}

ull get_next_round_key()
{
	uch v[128];
	rk_get_next_128bits(v);

	ull dec = to_decimal(v, 128);
	return dec;
}

void test_round_keys()
{
	for (int i = 0; i < 15; i++)
		printf("rki : %d, key : %lld\n", i, get_next_round_key());
}

uch statebytes[16];
int statectr = 0;
char *stateptr = NULL;

void state_load_next_128bits()
{
	// read 16 bytes
	for (int i = 0; i < 16; i++)
		statebytes[i] = 0;
	if (stateptr == NULL)
		stateptr = plaintextbuf;
	if (stateptr == plaintextptr)
		return;
	for (int i = 0; i < 16; i++)
	{
		if (*stateptr == '\0')
			statebytes[i] = 0;
		else
			statebytes[i] = *(stateptr++);
	}
}

void process_state_block(char input_block[], char output[]){
	
}

void test_state_load()
{
	// state_load_next_128bits();
	int iter_max = (plaintextptr - plaintextbuf)/16;
	for (int i = 0; i < iter_max; i++)
	{
		state_load_next_128bits();
		printf("i : %d, state block : '%s'\n", i, statebytes);
		uch encrypted_block[30];
		process_state_block(statebytes, encrypted_block);
	}
}

void runtests()
{
	read_key_from_file();
	split_key_to_32bit_words();
	get_expanded_key_words();
	read_plaintext_from_file();
	test_state_load();
	cleanup();
}
