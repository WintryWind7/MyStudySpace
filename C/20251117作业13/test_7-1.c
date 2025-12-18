#include <stdio.h>
#include <string.h>

void reverseWord(char *start, char *end);

int main()
{
    int T;
    char sentence[81];
    
    scanf("%d", &T);
    getchar();
    
    printf("T = %d\n", T);
    
    while (T--) {
        if (fgets(sentence, 81, stdin) == NULL) {
            printf("fgets failed\n");
            break;
        }
        
        printf("Read: [%s]\n", sentence);
        
        int len = strlen(sentence);
        if (sentence[len - 1] == '\n') {
            sentence[len - 1] = '\0';
            len--;
        }
        
        printf("After trim: [%s]\n", sentence);
        
        char *start = sentence;
        char *end = sentence;
        
        while (*end != '\0') {
            if (*end == ' ') {
                reverseWord(start, end - 1);
                start = end + 1;
            }
            end++;
        }
        reverseWord(start, end - 1);
        
        printf("%s\n", sentence);
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
