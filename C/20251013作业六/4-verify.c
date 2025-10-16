#include <stdio.h>

int main(){
    int n = 3;
    double sum = 1.0;
    double factorial = 1.0;
    
    for(int i = 1; i <= n; i++){
        factorial *= i;
        sum += 1.0 / factorial;
    }
    
    printf("标准方法: %.8f\n", sum);
    
    // 手工计算验证
    double manual = 1.0 + 1.0/1 + 1.0/2 + 1.0/6;
    printf("手工计算: %.8f\n", manual);
    
    return 0;
}
