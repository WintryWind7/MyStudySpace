#include <stdio.h>

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    
    int original_m = m, original_n = n;
    
    while (n != 0) {
        int temp = n;
        n = m % n;
        m = temp;
    }
    
    int gcd = m;
    int lcm = (original_m * original_n) / gcd;
    
    printf("%d %d\n", gcd, lcm);
    
    return 0;
}
