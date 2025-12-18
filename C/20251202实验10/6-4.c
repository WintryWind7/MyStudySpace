#include <stdio.h>

void FailStudent(FILE* in, FILE* out) {
    long long id;
    char name[101];
    int scores[3];
    const char *courseNames[3] = {"Math", "English", "C"};

    while (fscanf(in, "%lld %100s %d %d %d", &id, name, &scores[0], &scores[1], &scores[2]) == 5) {
        for (int i = 0; i < 3; ++i) {
            if (scores[i] < 60) {
                fprintf(out, "%lld %s %s\n", id, name, courseNames[i]);
            }
        }
    }
}
