#include <stdio.h>

int digitSum(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int N;
    scanf("%d", &N);
    
    for (int i = 0; i < N; i++) {
        int NA, NB;
        scanf("%d %d", &NA, &NB);
        
        int SA = digitSum(NA);
        int SB = digitSum(NB);
        
        // NA是SB的整数倍
        int A_is_dad = (SB != 0 && NA % SB == 0);
        // NB是SA的整数倍
        int B_is_dad = (SA != 0 && NB % SA == 0);
        
        if (A_is_dad && !B_is_dad) {
            printf("A\n");
        } else if (B_is_dad && !A_is_dad) {
            printf("B\n");
        } else {
            // 比较原始数字大小
            if (NA > NB) {
                printf("A\n");
            } else {
                printf("B\n");
            }
        }
    }
    
    return 0;
}
