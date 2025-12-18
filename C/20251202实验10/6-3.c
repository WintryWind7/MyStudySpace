#include <stdio.h>
#include <ctype.h>

int CountWord(FILE *file) {
    int ch;
    int inWord = 0;
    int count = 0;
    while ((ch = fgetc(file)) != EOF) {
        if (isalpha(ch)) {
            if (!inWord) {
                inWord = 1;
                ++count;
            }
        } else {
            inWord = 0;
        }
    }
    return count;
}
