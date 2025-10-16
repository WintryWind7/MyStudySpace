#include <stdio.h>
#include <math.h>

int main(){
    int n;
    scanf("%d", &n);
    int x=0, sum=0;
    while(n){
        sum += n%10;
        n/=10;
        x++;
    }
    printf("%d %d", x,sum);
    return 0;
}