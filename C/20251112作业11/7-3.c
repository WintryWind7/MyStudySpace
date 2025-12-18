#include <stdio.h>

int main()
{
    int n;
    if (scanf("%d", &n) != 1) {
        return 0;
    }
    int a[10];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    for (int i = 0; i < n - 1; i++) {
        int maxIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] > a[maxIndex]) {
                maxIndex = j;
            }
        }
        if (maxIndex != i) {
            int tmp = a[i];
            a[i] = a[maxIndex];
            a[maxIndex] = tmp;
        }
    }
    for (int i = 0; i < n; i++) {
        if (i) {
            printf(" ");
        }
        printf("%d", a[i]);
    }
    return 0;
}
