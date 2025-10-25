#include <stdio.h>

int gcd(int a, int b);

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d 和 %d 的最大公约数为: %d", a, b, gcd(a, b));
    return 0;
}

int gcd(int a, int b)
{
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}
