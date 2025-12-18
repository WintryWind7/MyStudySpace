#include <stdio.h>
#include <string.h>

int main()
{
    int T;
    char sentence[81];
    int i, j, k;
    char temp;
    
    scanf("%d", &T);
    getchar();
    
    while (T--) {
        fgets(sentence, 81, stdin);
        
        int len = strlen(sentence);
        if (len > 0 && sentence[len - 1] == '\n') {
            sentence[len - 1] = '\0';
            len--;
        }
        
        i = 0;
        while (i < len) {
            while (i < len && sentence[i] == ' ') {
                i++;
            }
            if (i >= len) break;
            
            j = i;
            while (j < len && sentence[j] != ' ') {
                j++;
            }
            
            int left = i;
            int right = j - 1;
            while (left < right) {
                temp = sentence[left];
                sentence[left] = sentence[right];
                sentence[right] = temp;
                left++;
                right--;
            }
            
            i = j;
        }
        
        printf("%s\n", sentence);
    }
    
    return 0;
}
