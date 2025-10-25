#include <stdio.h>

void reverse (int num);

int main() {
    reverse(12345);
    return 0;
}

void reverse (int num)
{
    if (num<10){
        printf("%d", num);
    }
    else{
        printf("%d", num%10);
        reverse(num/10);      
    }
}
