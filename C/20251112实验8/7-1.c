#include <stdio.h>
#include <string.h>

int main()
{
    char s[3][1001];
    char *p[3];
    for (int i = 0; i < 3; i++) {
        if (fgets(s[i], sizeof(s[i]), stdin) == NULL) {
            return 0;
        }
        size_t len = strlen(s[i]);
        if (len > 0 && s[i][len - 1] == '\n') {
            s[i][len - 1] = '\0';
        }
        p[i] = s[i];
    }

    for (int i = 0; i < 2; i++) {
        for (int j = i + 1; j < 3; j++) {
            if (strcmp(p[i], p[j]) > 0) {
                char *tmp = p[i];
                p[i] = p[j];
                p[j] = tmp;
            }
        }
    }

    for (int i = 0; i < 3; i++) {
        puts(p[i]);
    }

    return 0;
}
