#include <stdio.h>

int main() {
    double electricity;
    scanf("%lf", &electricity);
    
    if (electricity < 0) {
        printf("Invalid Value!\n");
    } else if (electricity <= 50) {
        printf("cost = %.2f\n", electricity * 0.53);
    } else {
        printf("cost = %.2f\n", 50 * 0.53 + (electricity - 50) * 0.58);
    }
    
    return 0;
}
