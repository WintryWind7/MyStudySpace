#include <stdio.h>

int main()
{
    int n;
    if (scanf("%d", &n) != 1) {
        return 0;
    }
    int nums[20];
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }
    int first = 1;
    for (int i = 0; i < n; i++) {
        int duplicate = 0;
        for (int j = 0; j < i; j++) {
            if (nums[j] == nums[i]) {
                duplicate = 1;
                break;
            }
        }
        if (!duplicate) {
            if (!first) {
                printf(" ");
            }
            printf("%d", nums[i]);
            first = 0;
        }
    }
    return 0;
}
