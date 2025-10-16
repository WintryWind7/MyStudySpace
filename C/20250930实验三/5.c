#include <stdio.h>

int main() {
    int year;
    scanf("%d", &year);
    
    if (year < 2001 || year > 2100) {
        printf("Invalid year!\n");
        return 0;
    }
    
    int found = 0;
    for (int i = 2001; i <= year; i++) {
        if ((i % 4 == 0 && i % 100 != 0) || (i % 400 == 0)) {
            printf("%d\n", i);
            found = 1;
        }
    }
    
    if (!found) {
        printf("None\n");
    }
    
    return 0;
}
