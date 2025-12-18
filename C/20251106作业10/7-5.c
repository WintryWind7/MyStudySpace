#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    double prices[101];
    int sold[101] = {0};
    
    for (int i = 1; i <= n; i++) {
        scanf("%lf", &prices[i]);
    }
    
    int type, bowls;
    double total = 0.0;
    
    while (scanf("%d %d", &type, &bowls)) {
        if (type == 0) break;
        sold[type] += bowls;
        total += prices[type] * bowls;
    }
    
    for (int i = 1; i <= n; i++) {
        printf("%d\n", sold[i]);
    }
    
    printf("%.2f\n", total);
    
    return 0;
}
