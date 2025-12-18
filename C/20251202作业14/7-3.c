#include <stdio.h>
#include <string.h>

typedef struct {
    char name[21];
    int score[3];
} Student;

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 0;
    }
    Student students[30];
    for (int i = 0; i < n; ++i) {
        if (scanf("%20s %d %d %d", students[i].name,
                  &students[i].score[0],
                  &students[i].score[1],
                  &students[i].score[2]) != 4) {
            return 0;
        }
    }
    char target[21];
    if (scanf("%20s", target) != 1) {
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        if (strcmp(students[i].name, target) == 0) {
            printf("%s: %d %d %d\n", students[i].name,
                   students[i].score[0], students[i].score[1], students[i].score[2]);
            return 0;
        }
    }

    printf("Null\n");
    return 0;
}
