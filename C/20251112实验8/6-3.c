#include <stdio.h>

int fun(char *ptr);

int main()
{
 char str[80];
 int s;
 gets(str);
 s=fun(str);
 printf("The new string is :");puts(str);
 printf("There are %d char in the new string.",s);
 return 0;
 }

int fun(char *ptr)
{
    int write = 0;
    int count = 0;
    for (int read = 0; ptr[read] != '\0'; read++) {
        if ((ptr[read] >= 'a' && ptr[read] <= 'z') || (ptr[read] >= 'A' && ptr[read] <= 'Z')) {
            ptr[write++] = ptr[read];
            count++;
        }
    }
    ptr[write] = '\0';
    return count;
}
