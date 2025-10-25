#include <stdio.h>

void hanoi(int n, char a, char b, char c);

int main() {
    int n;
    char a = '1', b = '2', c = '3';
    scanf("%d", &n);
    hanoi(n, a, b, c);
    printf("\n");
    return 0;
}

void hanoi(int n, char a, char b, char c)
{
    if (n == 1) {
        printf("%c->%c\n", a, c);
    } else {
        hanoi(n - 1, a, c, b);  // 将n-1个圆盘从a移动到b，c作为辅助
        printf("%c->%c\n", a, c);  // 将最大的圆盘从a移动到c
        hanoi(n - 1, b, a, c);  // 将n-1个圆盘从b移动到c，a作为辅助
    }
}
