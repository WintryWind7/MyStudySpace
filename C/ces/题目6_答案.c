#include <stdio.h>

struct Student {
    char name[20];
    char id[15];
    double score;
};

int main() {
    int n;
    scanf("%d", &n);
    
    struct Student students[50];
    double sum = 0;
    int maxIdx = 0, minIdx = 0;
    int failCount = 0;
    
    // 输入学生信息
    for (int i = 0; i < n; i++) {
        scanf("%s %s %lf", students[i].name, students[i].id, &students[i].score);
        sum += students[i].score;
        
        // 找最高分
        if (students[i].score > students[maxIdx].score) {
            maxIdx = i;
        }
        
        // 找最低分
        if (students[i].score < students[minIdx].score) {
            minIdx = i;
        }
        
        // 统计不及格
        if (students[i].score < 60) {
            failCount++;
        }
    }
    
    // 输出结果
    printf("average = %.2f\n", sum / n);
    printf("max: %s %.2f\n", students[maxIdx].name, students[maxIdx].score);
    printf("min: %s %.2f\n", students[minIdx].name, students[minIdx].score);
    printf("fail = %d\n", failCount);
    
    return 0;
}
