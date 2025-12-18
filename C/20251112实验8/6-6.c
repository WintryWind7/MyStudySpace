#include <stdio.h>

int StrCmp(const char *str1, const char *str2);

int main()
{
    char a[1024], b[1024];
    int r;
    gets(a);
    gets(b);
    r = StrCmp(a, b);
    if (r > 0)
    {
        puts("a > b");
    }
    else if (r < 0)
    {
        puts("a < b");
    }
    else
    {
        puts("a == b");
    }
    return 0;
}

int StrCmp(const char *str1, const char *str2)
{
    while (*str1 && (*str1 == *str2)) {
        str1++;
        str2++;
    }
    return (unsigned char)*str1 - (unsigned char)*str2;
}
