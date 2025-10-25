#include <stdio.h>
#include <math.h>
double f(double a,double b){
    return pow((a-cos(b))/2,0.5);
    //返回数学函数对应的表达式
}
int main() {
    double x;
    double y;
    x = f(1,0.5);//请使用参数1和0.5
    y = f(2,0.25);//请使用参数2和0.25
    printf("%.2f\n%.2f", x, y);
    return 0;
}