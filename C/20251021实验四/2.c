#include <stdio.h>
int wanshu(int x);

int main(){
    int b;
    for (int i=1;i<=1000;i++){
        b = wanshu(i);
        if (b==1)printf("%d是完数\n", i);
        
    }
}

int wanshu(int x){
    int sum=0;
    for (int j=1;j<x;j++){
        if (x%j==0){
                sum+=j;
        } 
    }
    if (sum==x)return 1;
    return 0;
}
