#include <stdio.h>

int fun(char s[], int num);

int main()
{
    char s[10];
    gets(s);
    fun(s, 8);
    printf("%s\n", s);
    return 0;
}

int fun(char s[], int num)
{
    for (int i = 0; i < num - 1; i++) {
        for (int j = i + 1; j < num; j++) {
            if (s[i] < s[j]) {
                char temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }
    return 0;
}
