#include <stdio.h>

static int is_narcissistic(int x) {
    int a = x / 100;
    int b = (x / 10) % 10;
    int c = x % 10;
    int sum = a * a * a + b * b * b + c * c * c;
    return sum == x;
}

int main(void) {
    int m, n;
    if (scanf("%d %d", &m, &n) != 2) {
        return 0;
    }

    FILE *out = fopen("out.txt", "w");
    if (!out) {
        return 0;
    }

    for (int i = m; i <= n; ++i) {
        if (is_narcissistic(i)) {
            fprintf(out, "%d ", i);
        }
    }

    fclose(out);
    return 0;
}
