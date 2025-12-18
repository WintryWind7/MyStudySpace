#include <stdio.h>

typedef struct {
    char name[9];
    double temperature;
    int cough;
} Patient;

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 0;
    }

    int count = 0;
    for (int i = 0; i < n; ++i) {
        Patient p;
        if (scanf("%8s %lf %d", p.name, &p.temperature, &p.cough) != 3) {
            return 0;
        }
        if (p.temperature >= 37.5 && p.cough == 1) {
            printf("%s\n", p.name);
            ++count;
        }
    }
    printf("%d\n", count);
    return 0;
}
