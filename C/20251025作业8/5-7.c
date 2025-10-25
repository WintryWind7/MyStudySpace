#include <stdio.h>
int fun (int m);
int main (void)
{   
    int n;
    
    scanf ("%d", &n);
    while (n > 0) {
        if (fun(n)) {
            printf("yes\n");
        }else{
            printf("No\n");
        }
        scanf("%d", &n);
    }
    
    return 0;
}

int fun (int m)
{   
    int cur_digit, old_digit = 10; 

    if (m < 0){
        m = -m;
    }
    do{
        cur_digit = m % 10;
        if( cur_digit >= old_digit){
            return 0;
        }
        old_digit = cur_digit;
        m = m / 10;
    }while (m != 0);
    
    return 1;
 }