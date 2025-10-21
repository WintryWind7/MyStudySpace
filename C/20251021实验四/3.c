#include <stdio.h>

int main(){
    int x,y,min;
    scanf("%d %d",&x,&y);
    if (x < y)min=x;
    else min=y;
    for (int i=min;i>0;i--){
        if ((x%i==0)&&(y%i==0)){
                printf("%d\n", i);
                break;
        } 
    }
}