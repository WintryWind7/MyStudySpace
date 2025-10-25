#include <stdio.h>

int SunFun(int n);
int f(int x);

int main(void) {
    printf("The sun=%d\n", SunFun(10));
    return 0;
}
int SunFun(int n) {
    int x, s;
    for (x = 0; x <= n; x++)
        s = s + f(x);
    return s;
}

int f(int x) {
    return x*x*x+1;
}