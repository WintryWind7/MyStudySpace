#include <stdio.h>

int main() {
    int a[10];
    int *p = a;
    
    for (int i = 0; i < 10; i++) {
        scanf("%d", p + i);
    }
    
    int max = *p;
    int min = *p;
    
    for (int i = 1; i < 10; i++) {
        if (*(p + i) > max) {
            max = *(p + i);
        }
        if (*(p + i) < min) {
            min = *(p + i);
        }
    }
    
    printf("difference value = %d\n", max - min);
    
    return 0;
}
