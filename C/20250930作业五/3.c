#include <stdio.h>

int main() {
    int level;
    double weight;
    scanf("%d %lf", &level, &weight);
    
    if (level == 1) {
        printf("%.2f\n", weight * 4.68);
    } else if (level == 2) {
        printf("%.2f\n", weight * 6.26);
    } else if (level == 3) {
        printf("%.2f\n", weight * 8.16);
    } else {
        printf("Not available!\n");
    }
    
    return 0;
}
