#include <stdio.h>

int main(){
    int M, N, a, b;
    scanf("%d %d",&M, &N);
    a = M;
    b = N;
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    printf("%d %d",a, M*N/a);
    return 0;
}