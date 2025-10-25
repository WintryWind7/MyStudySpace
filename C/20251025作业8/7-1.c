#include <stdio.h>

int isPrime(int n) {
    if (n <= 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int N;
    scanf("%d", &N);
    
    for (int p = 2; p <= N/2; p++) {
        if (isPrime(p)) {
            int q = N - p;
            if (isPrime(q)) {
                printf("%d = %d + %d\n", N, p, q);
                return 0;
            }
        }
    }
    
    return 0;
}
