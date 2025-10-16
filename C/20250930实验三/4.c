#include <stdio.h>

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    
    if (m < 100 || m > 999 || n < 100 || n > 999 || m > n) {
        printf("Invalid Value.\n");
        return 0;
    }
    
    for (int i = m; i <= n; i++) {
        int hundreds = i / 100;
        int tens = (i / 10) % 10;
        int units = i % 10;
        
        if (hundreds * hundreds * hundreds + tens * tens * tens + units * units * units == i) {
            printf("%d\n", i);
        }
    }
    
    return 0;
}
