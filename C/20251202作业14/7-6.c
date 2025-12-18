#include <stdio.h>

typedef struct {
    char name[21];
    int quantity;
    double price;
} Goods;

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 0;
    }

    double grandTotal = 0.0;
    Goods goods;
    for (int i = 0; i < n; ++i) {
        if (scanf("%20s %d %lf", goods.name, &goods.quantity, &goods.price) != 3) {
            return 0;
        }
        double total = goods.quantity * goods.price;
        grandTotal += total;
        printf("%s %d %.1f %.2f\n", goods.name, goods.quantity, goods.price, total);
    }
    printf("sum=%.2f\n", grandTotal);
    return 0;
}
