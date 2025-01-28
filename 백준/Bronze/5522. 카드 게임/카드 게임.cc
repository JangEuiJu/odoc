#include <stdio.h>

int main() {
    int num, i, sum=0;
    for(i=0; i<5; i++) {
        scanf("%d", &num);
        sum += num;
    }
    printf("%d", sum);
    return 0;
}