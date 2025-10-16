#include <stdio.h>

int main() {
    int Pa, Pb;
    int vote1, vote2, vote3;
    scanf("%d %d", &Pa, &Pb);
    scanf("%d %d %d", &vote1, &vote2, &vote3);
    
    int judgeA = 0, judgeB = 0;
    if (vote1 == 0) judgeA++;
    else judgeB++;
    if (vote2 == 0) judgeA++;
    else judgeB++;
    if (vote3 == 0) judgeA++;
    else judgeB++;
    
    if ((Pa > Pb && judgeA >= 1) || (Pa < Pb && judgeA == 3)) {
        printf("The winner is a: %d + %d\n", Pa, judgeA);
    } else {
        printf("The winner is b: %d + %d\n", Pb, judgeB);
    }
    
    return 0;
}
