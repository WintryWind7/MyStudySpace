#include <stdio.h>
#include <string.h>

int is_palindrome(const char *str)
{
    int left = 0;
    int right = (int)strlen(str) - 1;
    while (left < right) {
        if (str[left] != str[right]) {
            return 0;
        }
        left++;
        right--;
    }
    return 1;
}

int main()
{
    int n;
    if (scanf("%d", &n) != 1) {
        return 0;
    }
    getchar();
    char line[1024];
    for (int i = 0; i < n; i++) {
        if (fgets(line, sizeof(line), stdin) == NULL) {
            return 0;
        }
        size_t len = strlen(line);
        if (len > 0 && line[len - 1] == '\n') {
            line[len - 1] = '\0';
        }
        if (is_palindrome(line)) {
            puts("YES");
        } else {
            puts("NO");
        }
    }
    return 0;
}
