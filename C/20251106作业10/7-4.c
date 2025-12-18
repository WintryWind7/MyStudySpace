#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int monkeys[1001];
    for (int i = 1; i <= n; i++) {
        monkeys[i] = 1;
    }
    
    int count = n;
    int current = 1;
    int num = 0;
    
    while (count > 1) {
        if (monkeys[current] == 1) {
            num++;
            if (num == 3) {
                monkeys[current] = 0;
                count--;
                num = 0;
            }
        }
        current++;
        if (current > n) {
            current = 1;
        }
    }
    
    for (int i = 1; i <= n; i++) {
        if (monkeys[i] == 1) {
            printf("%d\n", i);
            break;
        }
    }
    
    return 0;
}
