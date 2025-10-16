#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    double sum = 0.0;
    int sign = 1;
    
    for (int i = 0; i < n; i++) {
        sum += sign * (1.0 / (1 + 3 * i));
        sign = -sign;
    }
    
    printf("sum = %.3f\n", sum);
    
    return 0;
}
