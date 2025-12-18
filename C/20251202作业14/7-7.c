#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

static Node *create_node(int data) {
    Node *node = (Node *)malloc(sizeof(Node));
    if (!node) {
        exit(1);
    }
    node->data = data;
    node->next = NULL;
    return node;
}

static void free_list(Node *head) {
    while (head) {
        Node *tmp = head;
        head = head->next;
        free(tmp);
    }
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n <= 0) {
        return 0;
    }

    Node *dummy = create_node(0);
    Node *tail = dummy;
    for (int i = 0; i < n; ++i) {
        int value;
        if (scanf("%d", &value) != 1) {
            free_list(dummy);
            return 0;
        }
        tail->next = create_node(value);
        tail = tail->next;
    }

    int m;
    if (scanf("%d", &m) != 1 || m < 0) {
        free_list(dummy);
        return 0;
    }

    for (int i = 0; i < m; ++i) {
        int op;
        if (scanf("%d", &op) != 1) {
            free_list(dummy);
            return 0;
        }
        if (op == 0) {
            int k, d;
            if (scanf("%d %d", &k, &d) != 2) {
                free_list(dummy);
                return 0;
            }
            Node *prev = dummy;
            int idx = 0;
            while (prev && idx < k) {
                prev = prev->next;
                ++idx;
            }
            if (!prev) {
                continue;
            }
            Node *node = create_node(d);
            node->next = prev->next;
            prev->next = node;
        } else if (op == 1) {
            int k;
            if (scanf("%d", &k) != 1) {
                free_list(dummy);
                return 0;
            }
            if (k <= 0) {
                continue;
            }
            Node *prev = dummy;
            int idx = 0;
            while (prev->next && idx < k - 1) {
                prev = prev->next;
                ++idx;
            }
            if (!prev->next) {
                continue;
            }
            Node *to_delete = prev->next;
            prev->next = to_delete->next;
            free(to_delete);
        } else {
            continue;
        }
    }

    Node *curr = dummy->next;
    while (curr) {
        printf("%d ", curr->data);
        curr = curr->next;
    }
    printf("\n");

    free_list(dummy);
    return 0;
}
