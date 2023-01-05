#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define LINE_LENGTH 1000
#define NWNUM 5
#define IS_SEP(c) (c == ' ' || c == ',' || c == ';' || c == ':')

int x_getline(char *s, int len)
{
    char *p = s, c;
    while ((c = getchar()) != '\n' && p - s < len)
        *p++ = c;
    *p = '\0';
    return p - s;
}

char *noise_words[NWNUM] = {
    "and", "or", "not", "for", "the"};

int is_noise_word(char t[])
{
    for (int i = 0; i < 5; i++)
        if (strcmp(t, noise_words[i]) == 0)
            return 1;
    return 0;
}

int word_array_ctr = 0;
char word_array[LINE_LENGTH][LINE_LENGTH];
char word_presence[LINE_LENGTH][LINE_LENGTH];

int find_wpos(char word[]){
    for(int i = 0; i < word_array_ctr; i++)
        if(strcmp(word_array[i], word) == 0) return i;
    return -1;
}

void log_word(char word[], int line_number)
{
    int wpos = find_wpos(word);
    if(wpos == -1){
        word_array_ctr += 1;
        wpos = word_array_ctr;
        strcpy(word_array[wpos], word);
    }
    char lnstr[1000];
    sprintf(lnstr, "%d", line_number);
    strcat(word_presence[wpos], lnstr);
    strcat(word_presence[wpos], ",");
}

int main(int argc, char **argv)
{
    for(int i = 0; i < LINE_LENGTH; i++){
        strcpy(word_array[i], "");
        strcpy(word_presence[i], "");
    }
    char s[LINE_LENGTH];
    int line_number = 0;
    while (x_getline(s, LINE_LENGTH) > 0)
    {
        int word_ctr = 0;
        int wfgate = 1;
        char word[LINE_LENGTH];
        char *p = s;
        while (*p != '\0' && *p != '\n')
        {
            char c = *p;
            if (IS_SEP(c))
            {
                if (wfgate == 0)
                {
                    word[word_ctr] = '\0';
                    word_ctr = 0;
                    if(!is_noise_word(word)) log_word(word, line_number);
                    wfgate = 1;
                }
            }
            else
            {
                wfgate = 0;
                word[word_ctr++] = c;
            }
            ++p;
        }
        line_number++;
    }
    for(int i = 1; i <= word_array_ctr; i++){
        printf("'%s' : %s\n", word_array[i], word_presence[i]);
    }
    return 0;
}