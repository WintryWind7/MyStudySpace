#include <stdio.h>

void deleted ( int a[], int n, int k);

int main()
{
    int a[9]={1,4,13,9,6,11,18,14,25},k;
    int i;
    scanf("%d",&k);
    deleted(a,9,k);
    for(i=0;i<8;i++)
         printf("%4d", a[i]);
    return 0;
}

void deleted(int a[], int n, int k) {
    for (int i = k; i < n - 1; i++) {
        a[i] = a[i + 1];
    }
}
