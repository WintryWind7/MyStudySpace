#include <stdio.h>

int digitalRoot(int n);

int main()
{
    int n;
    scanf("%d", &n);
    printf("%d\n", digitalRoot(n));
    return 0;
}

int digitalRoot(int n)
{
    int sum = 0;
    
    if (n < 10) {
        return n;
    }
    
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    
    return digitalRoot(sum);
}
