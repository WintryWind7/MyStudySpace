#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    double sum = 1.0;  // 第0项：1/0!
    double term = 1.0;  // 当前项的值：初始为1/0!

    for (int k = 1; k <= n; k++) {
        term /= k;      // term = 1/k!
        sum += term;    // 累加到总和
    }

    printf("%.8f\n", sum);
    return 0;
}