#include <stdio.h>

int main() {
    double r;
    scanf("%lf", &r);
    
    double s = 4 * 3.14159 * r * r;
    printf("s=%.2f\n", s);
    
    return 0;
}