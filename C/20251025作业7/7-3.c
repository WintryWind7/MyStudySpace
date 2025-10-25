#include <stdio.h>

// 判断是否为素数
int isPrime(int num)
{
    if (num < 2) return 0;
    if (num == 2) return 1;
    if (num % 2 == 0) return 0;
    
    for (int i = 3; i * i <= num; i += 2) {
        if (num % i == 0) return 0;
    }
    return 1;
}

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    
    int primes[1000];  // 存储素数
    int count = 0;     // 素数个数
    
    // 从n开始向下找素数
    for (int i = n; i >= 2 && count < k; i--) {
        if (isPrime(i)) {
            primes[count] = i;
            count++;
        }
    }
    
    // 输出结果
    int sum = 0;
    for (int i = 0; i < count; i++) {
        if (i > 0) printf("+");
        printf("%d", primes[i]);
        sum += primes[i];
    }
    printf("=%d\n", sum);
    
    return 0;
}

