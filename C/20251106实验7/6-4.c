#include <stdio.h>
#include <string.h>
#define MAXN 20

int Judge_char( char *s );

int main()
{
    char s[MAXN];
    
    scanf("%s", s);
    if ( Judge_char(s)==1 )
        printf("Yes\n");
    else
        printf("No\n");
    printf("%s\n", s);

    return 0;
}

int Judge_char(char *s) {
    int len = strlen(s);
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - 1 - i]) {
            return 0;
        }
    }
    return 1;
}

