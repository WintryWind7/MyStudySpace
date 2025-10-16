#include <stdio.h>

int main(){
    int n,sum=1;
    scanf("%d", &n);
    int a=1, b=1, c;
    sum = 0;
    int x = 0;
    while (sum<n){
        x++;
        if (x <3){
            sum = 1;
        }else if(x<5){
            sum += 1;
        }
        else{
            c = a+b;
            a=b, b=c;
            sum += c;
        }
        
        
    }
    printf("%d", x);
    return 0;
}