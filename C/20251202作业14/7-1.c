#include <stdio.h>

typedef struct {
    char name[21];
    double score;
} Student;

int main(void) {
    Student best = {"", -1.0};
    Student current;
    for (int i = 0; i < 5; ++i) {
        if (scanf("%20s %lf", current.name, &current.score) != 2) {
            return 0;
        }
        if (current.score > best.score) {
            best = current;
        }
    }
    printf("name = %s, score = %.1f\n", best.name, best.score);
    return 0;
}
