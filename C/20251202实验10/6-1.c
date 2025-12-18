#include <stdio.h>

void WriteArticle(FILE *f) {
    int ch;
    while ((ch = getchar()) != EOF) {
        if (fputc(ch, f) == EOF) {
            break;
        }
    }
}
