#include <stdio.h>
#include <stdlib.h>

int main(){
    int A, B, C, D;
    scanf("%d %d %d %d", &A, &B, &C, &D);
    printf("%d", abs((A+D) - (B+C)));
    return 0;
}