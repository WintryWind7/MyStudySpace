#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int a[20];
    a[0] = 1;
    a[1] = 2;
    
    for (int i = 2; i < n; i++) {
        a[i] = a[i-1] * a[i-2];
    }
    
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += a[i];
    }
    
    printf("sum = %d\n", sum);
    return 0;
}
