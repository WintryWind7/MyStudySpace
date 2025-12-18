#include <stdio.h>

typedef struct {
    char name[21];
    int volume;
    double price;
} Item;

int main(void) {
    int capacity, n;
    if (scanf("%d %d", &capacity, &n) != 2) {
        return 0;
    }

    Item best = {"", 0, -1.0};
    for (int i = 0; i < n; ++i) {
        Item item;
        if (scanf("%20s %d %lf", item.name, &item.volume, &item.price) != 3) {
            return 0;
        }
        if (item.volume <= capacity) {
            if (best.price < 0 || item.price < best.price) {
                best = item;
            }
        }
    }

    if (best.price >= 0) {
        printf("%s %d %.2f\n", best.name, best.volume, best.price);
    }

    return 0;
}
