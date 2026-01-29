#include <stdio.h>
#include <string.h>
#include <ctype.h>

int IsPalindrome(char str[]) {
    int len = strlen(str);
    int left = 0;
    int right = len - 1;
    
    while (left < right) {
        // 跳过非字母数字字符
        while (left < right && !isalnum(str[left])) {
            left++;
        }
        while (left < right && !isalnum(str[right])) {
            right--;
        }
        
        // 比较字符（忽略大小写）
        if (tolower(str[left]) != tolower(str[right])) {
            return 0;  // 不是回文
        }
        
        left++;
        right--;
    }
    
    return 1;  // 是回文
}

int main() {
    char str[101];
    fgets(str, 101, stdin);
    
    // 去掉换行符
    int len = strlen(str);
    if (str[len-1] == '\n') {
        str[len-1] = '\0';
    }
    
    if (IsPalindrome(str)) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    
    return 0;
}
