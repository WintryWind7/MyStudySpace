#include <stdio.h>

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    
    double sum = 0.0;
    
    for (int i = m; i <= n; i++) {
        sum += i * i + 1.0 / i;
    }
    
    printf("sum = %.6f\n", sum);
    
    return 0;
}
