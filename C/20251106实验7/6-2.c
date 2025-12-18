#include <stdio.h>

void fun(int score[],int n,int *b);

int main()
{
  int i,score[100],n,b[10];
 
  scanf("%d",&n);
    for(i=0;i<n;i++)
 scanf("%d",&score[i]);
    fun(score,n,b);
    for(i=0;i<10;i++)
  printf("%d ", b[i]);

  return 0;
}

void fun(int score[], int n, int *b) {
    for (int i = 0; i < 10; i++) {
        b[i] = 0;
    }
    
    for (int i = 0; i < n; i++) {
        if (score[i] >= 0 && score[i] <= 9) {
            b[0]++;
        } else if (score[i] >= 10 && score[i] <= 19) {
            b[1]++;
        } else if (score[i] >= 20 && score[i] <= 29) {
            b[2]++;
        } else if (score[i] >= 30 && score[i] <= 39) {
            b[3]++;
        } else if (score[i] >= 40 && score[i] <= 49) {
            b[4]++;
        } else if (score[i] >= 50 && score[i] <= 59) {
            b[5]++;
        } else if (score[i] >= 60 && score[i] <= 69) {
            b[6]++;
        } else if (score[i] >= 70 && score[i] <= 79) {
            b[7]++;
        } else if (score[i] >= 80 && score[i] <= 89) {
            b[8]++;
        } else if (score[i] >= 90 && score[i] <= 100) {
            b[9]++;
        }
    }
}

