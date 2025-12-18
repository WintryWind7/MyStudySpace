#include <stdio.h>
#define M 5

int fun(int a[M][M]) ;

int main()
{
  int a[M][M],i,j;
  int y;
  for(i=0;i<M;i++)
     for(j=0; j<M; j++)
            scanf("%d", &a[i][j])  ;
  y=fun(a);
  printf("sum=%d", y) ;
  return 0;
  }

int fun(int a[M][M])
{
    int sum = 0;
    for (int i = 0; i < M; i++) {
        sum += a[i][i];
        sum += a[i][M - 1 - i];
    }
    if (M % 2 == 1) {
        sum -= a[M / 2][M / 2];
    }
    return sum;
}
