#include <stdio.h>

void reverse(int a[], int start, int end) {
    while (start < end) {
        int temp = a[start];
        a[start] = a[end];
        a[end] = temp;
        start++;
        end--;
    }
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    
    int a[100];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    
    m = m % n;
    
    reverse(a, 0, n - 1);
    reverse(a, 0, m - 1);
    reverse(a, m, n - 1);
    
    for (int i = 0; i < n; i++) {
        if (i > 0) printf(" ");
        printf("%d", a[i]);
    }
    printf("\n");
    
    return 0;
}
