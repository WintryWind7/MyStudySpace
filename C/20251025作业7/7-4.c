#include <stdio.h>

int main()
{
    int height;
    scanf("%d", &height);
    
    // 检查高度是否为奇数
    if (height % 2 == 0) {
        printf("Error\n");
        return 0;
    }
    
    int mid = height / 2;  // 中间行的索引
    
    for (int i = 0; i < height; i++) {
        int spaces, width;
        
        if (i <= mid) {
            // 上半部分（包括中间行）
            spaces = mid - i;
            width = 2 * i + 1;
        } else {
            // 下半部分
            spaces = i - mid;
            width = 2 * (height - i - 1) + 1;
        }
        
        // 输出前导空格
        for (int j = 0; j < spaces; j++) {
            printf(" ");
        }
        
        // 输出菱形的一行
        if (width == 1) {
            // 顶点和底点
            printf("*");
        } else {
            // 空心部分
            printf("*");
            for (int j = 0; j < width - 2; j++) {
                printf(" ");
            }
            printf("*");
        }
        
        printf("\n");
    }
    
    return 0;
}

