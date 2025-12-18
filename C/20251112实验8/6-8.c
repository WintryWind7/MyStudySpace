#include <stdio.h>

int PutStr(const char *str);

int main()
{
    char a[1024];
    int n;
    gets(a);
    n = PutStr(a);
    printf("(%d)\n", n);
    return 0;
}

int PutStr(const char *str)
{
    int count = 0;
    while (*str) {
        putchar(*str++);
        count++;
    }
    return count;
}
