#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int count = 0;  // 数字个数
    int sum = 0;    // 数字和
    int even = 0;   // 偶数个数
    
    int temp = n;
    while (temp > 0) {
        int digit = temp % 10;  // 取最后一位
        count++;
        sum += digit;
        if (digit % 2 == 0) {
            even++;
        }
        temp /= 10;  // 去掉最后一位
    }
    
    printf("count = %d\n", count);
    printf("sum = %d\n", sum);
    printf("even = %d\n", even);
    
    return 0;
}
