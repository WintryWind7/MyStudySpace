#include <stdio.h>

void ReadArticle(FILE *f) {
    int ch;
    while ((ch = fgetc(f)) != EOF) {
        putchar(ch);
    }
}
