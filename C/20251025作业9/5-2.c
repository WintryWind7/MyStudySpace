#include <stdio.h>

double sum(int n);

int main() {
    printf("%f", sum(10));
    return 0;
}

double sum(int n){
    if (n == 0){ 
        return 0;
    }
    else{
        return sum(n-1) + n;
    }
}