#include <stdio.h>

void fun(char str[]);

int main()
{
    char str[20];

    scanf("%s", str);
    fun(str);
    printf("%s", str);

    return 0;
}

void fun(char str[])
{
    int i, j, k;
    int len = 0;
    
    while (str[len] != '\0') {
        len++;
    }
    
    for (i = 0; i < len; i++) {
        for (j = i + 1; j < len; j++) {
            if (str[i] == str[j]) {
                for (k = j; k < len; k++) {
                    str[k] = str[k + 1];
                }
                len--;
                j--;
            }
        }
    }
}
