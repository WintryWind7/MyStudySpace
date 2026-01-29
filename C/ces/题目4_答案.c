#include <stdio.h>

void Transpose(int matrix[][10], int result[][10], int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[j][i] = matrix[i][j];
        }
    }
}

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    
    int matrix[10][10];
    int result[10][10];
    
    // 输入矩阵
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    
    // 转置
    Transpose(matrix, result, m, n);
    
    // 输出转置后的矩阵
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d", result[i][j]);
            if (j < m - 1) printf(" ");
        }
        printf("\n");
    }
    
    return 0;
}
