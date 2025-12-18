#include "stdio.h"

void fun(char *str) ;

int main()
{
  char str[81] ;
  gets(str) ;
  fun(str) ;
  printf("%s",str) ;
  return 0;
}

void fun(char *str)
{
    int write = 0;
    for (int read = 0; str[read] != '\0'; read++) {
        if (str[read] != ' ') {
            str[write++] = str[read];
        }
    }
    str[write] = '\0';
}
