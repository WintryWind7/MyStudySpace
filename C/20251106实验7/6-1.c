#include<stdio.h>
#define N 12

int  findX(int *p,int n,int x);

int  main()
{
    int a[N];
    int i,x;
    int iRet;
    
    for(i=0; i<N;i++) 
      iRet = scanf("%d", &a[i]);
    iRet = scanf("%d",&x);
    
    iRet=findX(a,12,x);
    
    if ( iRet < 0)
      printf("Not Found\n");
    else
      printf("index=%d,value=%d" ,iRet ,a[iRet]);
}

int findX(int *p, int n, int x) {
    int lastIndex = -2;
    for (int i = 0; i < n; i++) {
        if (p[i] == x) {
            lastIndex = i;
        }
    }
    return lastIndex;
}

