#include <stdio.h>
#include <math.h>

int main(){
    int a,n;
    scanf("%d %d",&a, &n);
    double sum;
    int temp = 0;
    for (int i = 0; i < n; i++){

        temp += a*pow(10, i);

        if (i == n-1){
            sum += temp;
        }else{
            sum += 2*temp;  // 题目出错了
        }
        
    }
    printf("sum=%.f",sum);
    return 0;
}