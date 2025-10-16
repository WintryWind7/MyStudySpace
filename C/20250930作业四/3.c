#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int cycle = n % 5;
    if (cycle == 0) cycle = 5;
    
    if (cycle <= 3) {
        printf("Fishing in day %d\n", n);
    } else {
        printf("Drying in day %d\n", n);
    }
    
    return 0;
}
