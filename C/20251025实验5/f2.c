#include <stdio.h>

int fib(int n);

int main() {
    int n;
    scanf("%d", &n);
    printf("num = %d", fib(n));
    return 0;
}

int fib(int n)
{
    if (n == 1 || n == 2) {
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}
