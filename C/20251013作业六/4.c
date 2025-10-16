#include <stdio.h>

int main(){
    int n,i;
    scanf("%d", &n);
    double fz,fm=1;
    for (i=1;i<=n;i++){
        fm *= i;
    }
    int t = fm;
    
    fz = fm;
    i = 1;
    
    while (t!=1){
        t/=++i;
        fz += t;
        
    }

    printf("%.8f", (fz+fm)/fm);
    return 0;
}