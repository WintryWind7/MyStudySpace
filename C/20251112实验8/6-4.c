#include <stdio.h>

int StrLen(const char *str);

int main()
{
    char s[1024];
    int n;
    gets(s);
    n = StrLen(s);
    printf("%d\n", n);
    return 0;
}

int StrLen(const char *str)
{
    int len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}
