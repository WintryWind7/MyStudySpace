#include <stdio.h>
#include <string.h>

void SortStrings(char str[][50], int n) {
    char temp[50];
    
    // 冒泡排序
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (strcmp(str[j], str[j+1]) > 0) {
                // 交换字符串
                strcpy(temp, str[j]);
                strcpy(str[j], str[j+1]);
                strcpy(str[j+1], temp);
            }
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    getchar();  // 吃掉换行符
    
    char strings[20][50];
    
    // 输入字符串
    for (int i = 0; i < n; i++) {
        fgets(strings[i], 50, stdin);
        // 去掉换行符
        int len = strlen(strings[i]);
        if (strings[i][len-1] == '\n') {
            strings[i][len-1] = '\0';
        }
    }
    
    // 排序
    SortStrings(strings, n);
    
    // 输出
    for (int i = 0; i < n; i++) {
        printf("%s\n", strings[i]);
    }
    
    return 0;
}
