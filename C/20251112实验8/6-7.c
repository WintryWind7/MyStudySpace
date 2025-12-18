#include <stdio.h>

char* StrChr(const char *str, char chr);

int main()
{
    char s[1024], x, *p;
    gets(s);
    x = getchar();
    p = StrChr(s, x);
    if (p)
    {
        printf("Found at %d\n", (int)(p - s));
    }
    else
    {
        puts("Not found");
    }
    return 0;
}

char* StrChr(const char *str, char chr)
{
    while (*str) {
        if (*str == chr) {
            return (char *)str;
        }
        str++;
    }
    return NULL;
}
