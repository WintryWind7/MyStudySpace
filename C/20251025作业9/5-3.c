#include <stdio.h>

void Porder(int n);
int main()
{
    int num;
    scanf("%d",&num);
    Porder(num);
    return 0;
}

void Porder(int n){
    if (n>10){
        Porder(n/10);
    }
    printf("%d\n", n%10);
}