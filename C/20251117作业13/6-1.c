#include <stdio.h>
#include <ctype.h>
#define MAXS 15

void StringCount( char s[] );
void ReadString( char s[] );

int main()
{
    char s[MAXS];

    ReadString(s);
    StringCount(s);

    return 0;
}

void ReadString( char s[] )
{
    int i = 0;
    char c;
    while ((c = getchar()) != '\n' && i < MAXS - 1) {
        s[i++] = c;
    }
    s[i] = '\0';
}

void StringCount( char s[] )
{
    int letter = 0, blank = 0, digit = 0, other = 0;
    int i = 0;
    
    while (s[i] != '\0') {
        if (isalpha(s[i])) {
            letter++;
        } else if (s[i] == ' ' || s[i] == '\n' || s[i] == '\r') {
            blank++;
        } else if (isdigit(s[i])) {
            digit++;
        } else {
            other++;
        }
        i++;
    }
    
    printf("letter = %d, blank = %d, digit = %d, other = %d\n", 
           letter, blank, digit, other);
}
