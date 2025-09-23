#include <stdio.h>

int main() {
    int i, tmp, sum = 0;
    for(i=0; i<4; i++) {
        scanf("%d", &tmp);
        sum += tmp;
    }
    printf("%d\n", sum/60);
    printf("%d\n", sum%60);
    return 0;
}