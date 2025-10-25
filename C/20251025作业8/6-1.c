#include <stdio.h>
#include <math.h>

double fact(int n){
    double result=1;
    for (int i=1;i<=n;i++){
        result*=i;
    }
    return result;
}

double MySin(double x, double epsilon){
    double result = 0, t;
    int i = 1, sign = 1;
    while(1){
        t = sign * pow(x, i) / fact(i);
        if (fabs(t) < epsilon){
            break;
        }
        result += t;
        sign = -sign;
        i+=2;
    }
    return result;
}

int main()
{
    double x,epsilon;
    scanf("%lf%lf",&x,&epsilon);
    printf("%.15f\n",MySin(x,epsilon));
    return 0;
}