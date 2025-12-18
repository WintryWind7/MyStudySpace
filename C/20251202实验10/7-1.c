#include <stdio.h>
#include <math.h>

static int is_prime(int x) {
    if (x < 2) {
        return 0;
    }
    if (x == 2) {
        return 1;
    }
    if (x % 2 == 0) {
        return 0;
    }
    int limit = (int)sqrt((double)x);
    for (int i = 3; i <= limit; i += 2) {
        if (x % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main(void) {
    FILE *in = fopen("in.txt", "r");
    if (!in) {
        return 0;
    }
    FILE *out = fopen("out.txt", "w");
    if (!out) {
        fclose(in);
        return 0;
    }

    int value;
    long long sum = 0;
    int count = 0;
    while (fscanf(in, "%d", &value) == 1) {
        if (is_prime(value)) {
            sum += value;
            ++count;
        }
    }

    double avg = 0.0;
    if (count > 0) {
        avg = (double)sum / count;
    }
    fprintf(out, "%.2f", avg);

    fclose(in);
    fclose(out);
    return 0;
}
