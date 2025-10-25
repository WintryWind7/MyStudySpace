#include <stdio.h>

double fun(int n){
    double t=1.0;
    int i;
    for(i=2; i<=n; i++)
    t = t + 1.0/i;
    return t;
}

int main(void){
    int m;
    double s;
    scanf("%d",&m);
    s = fun(m);  //调用函数
    printf("%.3f", s);
    return 0;
}