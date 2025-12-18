#include <stdio.h>

char* StrCpy(char *dst, const char *src);

int main()
{
    char a[1024], b[1024];
    gets(a);
    StrCpy(b, a);
    puts(b);
    return 0;
}

char* StrCpy(char *dst, const char *src)
{
    char *ret = dst;
    while (*src) {
        *dst++ = *src++;
    }
    *dst = '\0';
    return ret;
}
