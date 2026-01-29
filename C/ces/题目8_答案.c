#include <stdio.h>

// 矩阵加法
void MatrixAdd(int *a, int *b, int *c, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            *(c + i*cols + j) = *(a + i*cols + j) + *(b + i*cols + j);
        }
    }
}

// 矩阵乘法
void MatrixMultiply(int *a, int *b, int *c, int m, int n, int p) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            *(c + i*p + j) = 0;
            for (int k = 0; k < n; k++) {
                *(c + i*p + j) += *(a + i*n + k) * *(b + k*p + j);
            }
        }
    }
}

int main() {
    int op;
    scanf("%d", &op);
    
    if (op == 1) {
        // 矩阵加法
        int m, n;
        scanf("%d %d", &m, &n);
        
        int a[10][10], b[10][10], c[10][10];
        
        // 输入矩阵A
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                scanf("%d", &a[i][j]);
            }
        }
        
        // 输入矩阵B
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                scanf("%d", &b[i][j]);
            }
        }
        
        // 计算A+B
        MatrixAdd((int *)a, (int *)b, (int *)c, m, n);
        
        // 输出结果
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                printf("%d", c[i][j]);
                if (j < n - 1) printf(" ");
            }
            printf("\n");
        }
        
    } else if (op == 2) {
        // 矩阵乘法
        int m, n, p;
        scanf("%d %d %d", &m, &n, &p);
        
        int a[10][10], b[10][10], c[10][10];
        
        // 输入矩阵A (m×n)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                scanf("%d", &a[i][j]);
            }
        }
        
        // 输入矩阵B (n×p)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                scanf("%d", &b[i][j]);
            }
        }
        
        // 计算A×B
        MatrixMultiply((int *)a, (int *)b, (int *)c, m, n, p);
        
        // 输出结果 (m×p)
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < p; j++) {
                printf("%d", c[i][j]);
                if (j < p - 1) printf(" ");
            }
            printf("\n");
        }
    }
    
    return 0;
}
