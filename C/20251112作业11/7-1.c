#include <stdio.h>

int main()
{
    int n;
    if (scanf("%d", &n) != 1) {
        return 0;
    }
    int matrix[10][10];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    int sum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            sum += matrix[i][j];
        }
    }
    printf("%d", sum);
    return 0;
}
