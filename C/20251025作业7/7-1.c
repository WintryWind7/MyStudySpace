#include <stdio.h>

int main()
{
    int heads, feet;
    scanf("%d %d", &heads, &feet);
    
    // 设鸡为x只，兔为y只
    // x + y = heads
    // 2x + 4y = feet
    // 解得：x = 2*heads - feet/2, y = feet/2 - heads
    
    // 检查是否有整数解
    if (feet % 2 != 0) {
        printf("No solution!\n");
        return 0;
    }
    
    int chickens = 2 * heads - feet / 2;
    int rabbits = feet / 2 - heads;
    
    // 检查解是否为非负整数
    if (chickens >= 0 && rabbits >= 0) {
        printf("chickens = %d; rabbits = %d\n", chickens, rabbits);
    } else {
        printf("No solution!\n");
    }
    
    return 0;
}

