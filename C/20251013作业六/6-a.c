#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    
    int month = 1;
    int prev = 1, curr = 1;  // 前两个月都是1对兔子
    
    // 如果n<=1，第1个月就达到了
    if(n <= 1) {
        printf("%d\n", 1);
        return 0;
    }
    
    // 从第2个月开始检查
    while(curr < n) {
        month++;
        if(month <= 2) {
            curr = 1;  // 第1、2个月都是1对
        } else {
            int next = prev + curr;  // 斐波那契递推
            prev = curr;
            curr = next;
        }
    }
    
    printf("%d\n", month);
    return 0;
}
