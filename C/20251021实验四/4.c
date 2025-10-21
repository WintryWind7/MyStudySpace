#include <stdio.h>
int main(){
    int n;
    scanf("%d", &n);
    if (n>0){
        if (sushu(n)==1){
            printf("%d", reverse(n));
        }else{
            printf("%d", he(n));
        }
        
    }else return 0;
}

int reverse(int number){
    int digit, res;
    res = 0;
    do{
        digit = number % 10;
        res = 10*res + digit;
        number /= 10;
    }while (number != 0);

    return res;
}

int sushu(int x){
    for (int i=2;i<x;i++){
        if (x%i==0)return 0;
    }
    return 1;    
}

int he(int num){
    int sum=0;
    while (num!=0){
        sum += num%10;
        num /= 10;
    }
    return sum;
}