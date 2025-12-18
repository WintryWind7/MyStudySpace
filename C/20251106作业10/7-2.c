#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int count[11] = {0};
    
    for (int i = 0; i < n; i++) {
        int score;
        scanf("%d", &score);
        
        if (score >= 0 && score <= 100) {
            if (score < 10) {
                count[0]++;
            } else if (score == 100) {
                count[10]++;
            } else {
                count[score / 10]++;
            }
        }
    }
    
    for (int i = 0; i < 11; i++) {
        printf("%d: %d\n", i, count[i]);
    }
    
    return 0;
}
