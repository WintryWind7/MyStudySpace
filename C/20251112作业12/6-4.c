# include<stdio.h>
int Bsearch(int *p, int n, int x);     
int main(void)   
{
    int a[10] = {1,2,3,4,5,6,7,8,9,10};    
    int x, m;
    scanf("%d",&x);                
    m = Bsearch(a, 10, x);
    if(m >= 0)   
        printf("Index is %d\n",m);
    else 
        printf( "Not Found\n");
        
    return 0;
}

int Bsearch(int *p, int n, int x)
{
    int left = 0;
    int right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (p[mid] == x) {
            return mid;
        } else if (p[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
