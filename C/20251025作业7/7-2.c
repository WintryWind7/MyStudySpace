#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        char ticket[7];
        scanf("%s", ticket);
        
        // 计算前3位数字之和
        int sum1 = (ticket[0] - '0') + (ticket[1] - '0') + (ticket[2] - '0');
        
        // 计算后3位数字之和
        int sum2 = (ticket[3] - '0') + (ticket[4] - '0') + (ticket[5] - '0');
        
        if (sum1 == sum2) {
            printf("You are lucky!\n");
        } else {
            printf("Wish you good luck.\n");
        }
    }
    
    return 0;
}

