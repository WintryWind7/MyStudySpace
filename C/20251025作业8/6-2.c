#include <stdio.h>
#include <math.h>

int search( int n );

int main()
{
    int number;

    scanf("%d",&number);
    printf("count=%d\n",search(number));
        
    return 0;
}

int search( int n ) {
    int count = 0;
    
    for (int i = 101; i <= n; i++) {
        // 检查是否为完全平方数
        int sqrt_i = (int)sqrt(i);
        if (sqrt_i * sqrt_i == i) {
            int digit1 = i / 100;        // 百
            int digit2 = (i / 10) % 10;  // 十
            int digit3 = i % 10;         // 个
            
            if (digit1 == digit2 || digit1 == digit3 || digit2 == digit3) {
                count++;
            }
        }
    }
    
    return count;
}
