#include <stdio.h>
#include <string.h>

void reverseWord(char *start, char *end);

int main()
{
    int T;
    char sentence[81];
    int i, j;
    
    scanf("%d", &T);
    getchar();
    
    while (T--) {
        fgets(sentence, 81, stdin);
        
        int len = strlen(sentence);
        if (len > 0 && sentence[len - 1] == '\n') {
            sentence[len - 1] = '\0';
            len--;
        }
        
        printf("Input: [%s]\n", sentence);
        
        i = 0;
        while (i < len) {
            if (sentence[i] == ' ') {
                i++;
                continue;
            }
            j = i;
            while (j < len && sentence[j] != ' ') {
                j++;
            }
            printf("Reversing from %d to %d: [", i, j-1);
            for (int k = i; k < j; k++) printf("%c", sentence[k]);
            printf("]\n");
            
            if (j > i) {
                reverseWord(&sentence[i], &sentence[j - 1]);
            }
            i = j;
        }
        
        printf("Output: %s\n", sentence);
    }
    
    return 0;
}

void reverseWord(char *start, char *end)
{
    char temp;
    while (start < end) {
        temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}
