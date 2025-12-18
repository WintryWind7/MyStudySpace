#include <stdio.h>
#include <string.h>

long fun ( char *p);

int main()
{ 
    char s[6];
    long n;
    scanf("%s", s);
    n = fun(s);
    printf("%ld", n);
    return 0;
}

long fun ( char *p)
{
    long result = 0;
    int sign = 1;
    int i = 0;
    
    if (p[0] == '-') {
        sign = -1;
        i = 1;
    } else if (p[0] == '+') {
        i = 1;
    }
    
    while (p[i] != '\0') {
        result = result * 10 + (p[i] - '0');
        i++;
    }
    
    return result * sign;
}
