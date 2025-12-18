#include <stdio.h>
void bubble (int a[ ], int n);
int main(void)
{    
  int n, a[10];
    int i;
    scanf("%d", &n);
    for (i=0; i<n;i++)
        scanf("%d",&a[i]);
    bubble(a,n);
    for (i=0; i<n; i++)
        printf("%d ",a[i]);
  printf("\n");
    return 0;
}

void bubble(int a[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
}
