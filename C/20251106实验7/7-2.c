#include <stdio.h>

void calculate(int (*scores)[5], int m, int n) {
    for (int i = 0; i < m; i++) {
        int sum = 0;
        for (int j = 0; j < n; j++) {
            sum += *(*(scores + i) + j);
        }
        double average = (double)sum / n;
        printf("%d %.1f\n", sum, average);
    }
}

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    
    int scores[30][5];
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", *(scores + i) + j);
        }
    }
    
    calculate(scores, m, n);
    
    return 0;
}

